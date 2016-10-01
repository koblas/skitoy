---
title: React and GraphQL, plus GoLang
author: koblas
layout: post
date: 2016-09-30T21:53:24+00:00
url: /p/react-to-graphql/629
pvc_views:
  - 98
categories:
  - Development
tags:
  - react
  - graphql
  - redux
  - golang

---

This is some useful inisights I've gained, that are worth noting. The code examples are from a gist clone that I'm playing around with, it's easier to have a "known" problem and target to experiment with software than trying to do both at the same time.

### React

What's clear is that with appropriate use of PropTypes, you really have a well structured "strict" environment for building components. It's nice to see that when you pass the wrong parameter into a directive that it fails fast. On my agenda is to move my ES6 codebase over to TypeScript to see what having and even more strictly typed environment does.

React is good that it's helping put the motivation under JS and the practices of front end development to have stronger types which reduce errors in the long run. I see this in my Go code frequently, where a fumble finger would have created a new variable or assigned it to the wrong thing.

What's interesting is when React decides to change the life cycle of a component and the additional work that you need to do when that component is the main view. This was a recent example of that.

    constructor(props) {
        super(props)

        const { user, guid } = props.params

        this.state = this._build_state(guid, user)
    }

    componentWillMount() {
        this._fetch(this.state.guid, this.state.user)
    }

    componentWillReceiveProps(nextProps) {
        const { user, guid } = nextProps.params

        this.setState(this._build_state(user, guid))
        this._fetch(user, guid)
    }

### GraphQL

Provides a strongly typed well defined API schema that once you wrap your head around the queries, mutations slightly weird libraries and packages that hold it all together it's pretty darn cool. 

For instance it's easy to define the following type structure:

    type User {
        id          String!
        username    String!
        email       String!
        first_name  String
        last_name   String
        image_url   String

        gists(id: String)   [Gist]
    }
      
    type Gist {
        id       String!
        title    String
        version  String!
        files    [GistFile]
    }
      
    type GistFile {
        id       String!
        version  String!
        name     String
        body     String
    }
      
What's really nice is the API now is defined to say what's required fields and I can also ask for a single Gist (which returns a list of 0 or 1 elements). In one API call I can get the user information, their 5 most recent gist (ok, that API isn't there yet) and the files that it represents.

### Redux

I've finally gotten my head around how to use ``@connect((state) => { ... }`` correctly. It's amazingly powerful, to have components react to changes. For instance when you log into the application the "App" knows to go refetch the use information to surface (e.g. that drop menu with your avatar attached).

    @connect((state) => {
        return {
            dispatch: state.dispatch,
            isAuthenticated: state.auth.isAuthenticated,
        }
    })
    class App extends Component {
        static propTypes = {
            dispatch: PropTypes.func.isRequired,
            isAuthenticated: PropTypes.bool.isRequired,
        }

        componentWillMount() {
            const { dispatch, isAuthenticated } = this.props

            if (isAuthenticated)
                dispatch(getUserData(client))
        }

        componentWillReceiveProps(nextProps) {
            const { dispatch, isAuthenticated } = this.props

            if (nextProps.isAuthenticated != isAuthenticated) {
                if (nextProps.isAuthenticated) {
                    dispatch(getUserData(client))
                } else {
                    dispatch(clearUserData())
                }
            }
        }

        //....
    }


### Golang + GraphQL

As you may already know the key idea of GraphQL is that you can dispatch a single query and get back a fairly extensive result, rather than making 37 different REST calls to fetch the same data, or maybe have lots of parameters to an API to include and exclude specific things.

If you read back through some of my blog posts, I spent a great deal of time polishing rocks working on an API design. Well as soon as I dropped in the GraphQL library which has it's own world view, those got tossed out the window. I'm back to having "200" success and "400" for something went wrong, including the object wasn't found.

However, the really great part about the graphql-go library is the way that it lets you defer the fetching of data. So for instance that type system you see above, the DB call to fetch the file isn't made unless you ask for it and it's easy to have a single structured API to handle it.

    "files": &graphql.Field{
        Type: graphql.NewList(gistFileType),
        Resolve: graphqlResolve(func(ctx graphqlContext) (interface{}, error) {
            gist := ctx.params.Source.(*models.Gist)

            if err := gist.LoadFiles(); err != nil {
                ctx.logger.With(
                    zap.String("id", gist.Guid),
                    zap.Error(err),
                ).Error("unable to get gist files")
                return nil, err
            }

            return gist.Files, nil
        }),
    },

That's almost magic, it will only take about 10 minutes to add "offset" and "count" arguments for files. The only "ugly" side of the graphql-go library is on the Input side -- side note: it took me way to long to understand that there are Input types that are distinct from Output types. For simple arguments everything is "easy", the challenge is that when you post back up a Gist + Files, there is no way to have the library marshal it into an object structure for you (at least that I've found). So you end up with some warty code like:

    gist.Files = make([]*models.GistFile, 0)

    for _, file := range files {
        data, ok := file.(map[string]interface{})
        if !ok {
            // TODO: Bad type, do something
        }

        f := gist.NewFile()

        for k, v := range data {
            switch k {
            //case "id":
            //    f.Guid = v.(string)
            case "name":
                f.Name = strings.TrimSpace(v.(string))
            case "body":
                f.Body = v.(string)
            }
        }
        
        // ... code removed ...
    }
    
### Parting thought

It takes time to really get comfortable with something, it's really nice to have the time to dig into this and really get a complete understanding. I'm really excited that it's so "easy" to create rich single page apps.
