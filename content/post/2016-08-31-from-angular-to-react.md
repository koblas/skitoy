---
title: From Angular to React
author: koblas
layout: post
date: 2016-08-31T19:53:24+00:00
url: /p/from-angular-to-react/628
pvc_views:
  - 98
categories:
  - Development
tags:
  - react

---
If you ever looked at my github &#8211; public or private you can see that I have settled on a personal template for Angular applications. While I&#8217;m sure that there are things that are against some blog post of conventions, it works and gets lots of jobs done. After digging into the performance of our SPA at Tubular I found that we were spending 1.5 seconds rendering the results of an XHR (Ajax) requests to fetch some data.

Yes, our Angular application was taking 1.5 seconds to render 15 result items and a list (about 15 facts) of the search each having about 5 items. That&#8217;s totally crazy. Like anybody you crack open the blog posts on performance and read and fix and read and fix until you realize that this is a huge undertaking that has to do with the way that data is bound in Angular and it&#8217;s really easy to get an application working it really hard to get the performance back if you didn&#8217;t take care of it from day one.

### Enter React

What I found is that a few people encourage the use of React to take over the rendering from Angular. Learning React is something that I&#8217;ve been putting off for a while, I built one quick React-native application but will admit that I didn&#8217;t fully understand what I was working with. So, I took my latest project (not public) and started recoding the application from Angular to React+Redux.

### Learnings

There are way too many blog posts take build the ToDo application, or overly simple React applications that don&#8217;t end up with all of the real problems that an application has.

For starters &#8211;

<img width="242" height="300" src="/uploads/2016/08/Screen-Shot-2016-08-31-at-12.08.47-PM.png" alt="Login Content" />

Is a fairly complicated React application, it involves:

  * React
  * React-Router
  * Redux
  * AJAX (via axios in my case)
  * Validation
  * Build system (something to generate app.js from all of the files)
  * Plus a bunch of other things (Material-UI to make it look pretty)

Once you have it all working, it looks pretty simple and it does make sense when you read the code.  Some key snippets:

Login.jsx &#8212; This is the react View

```javascript
import React, { Component, PropTypes } from 'react'
import { TextField, Checkbox, FlatButton, RaisedButton, FontIcon } from 'material-ui';
import { Link } from 'react-router';
import { AuthBox, AuthHeader, AuthBody, AuthError } from './AuthBox'
import validator from 'validator'
import { resetLogin, loginUser, logoutUser } from './actions'

export default class Login extends Component {
    static contextTypes = {
        dispatch: PropTypes.func.isRequired,
        store: PropTypes.object.isRequired,
    }

    constructor() {
        super()

        this.state = {
            email: undefined,
            password: undefined,
            remember: true,
        }

        this._submit = this._submit.bind(this)
        this._set_remember = this._set_remember.bind(this)
        this._set_email = this._set_email.bind(this)
        this._set_password = this._set_password.bind(this)
    }

    componentWillMount() {
        this.context.dispatch(resetLogin())
        // If you are on the login page, lets clear the state to make sure you can login
        this.context.dispatch(logoutUser())
    }

    _submit(event) {
        event.preventDefault()

        var next = this.props.location.query.next

        this.context.dispatch(loginUser({
                email: this.state.email, 
                password: this.state.password, 
                remember: this.state.remember
            }, next))
    }

    // Checkbox to remember this user
    _set_remember(event, isInputChecked) {
        this.setState({remember: isInputChecked})
    }

    _set_email(event) {
        this.setState({email: event.target.value})
    }

    _set_password(event) {
        this.setState({password: event.target.value})
    }

    _validate() {
        var valid = true

        var update = {
            ready: false,
            email_error: undefined,
            password_error: undefined,
        }

        if (this.state.email != undefined) {
            var email = validator.trim(this.state.email)
            if (email.length == 0) {
                update.email_error = "Please enter your email"
                valid = false
            } else if (!validator.isEmail(email)) {
                update.email_error = "Invalid email address"
                valid = false
            }
        } else {
            valid = false
        }

        if (this.state.password != undefined) {
            var password = validator.trim(this.state.password)
            if (password.length < 8) {
                update.password_error = "Passwords must be at least 8 characters"
                valid = false
            }
        } else {
            valid = false
        }

        update.ready = valid
        return update
    }

    render() {
        const valid = this._validate()
        console.log(valid)
        
        return (
            <AuthBox title="Login">
      <AuthBody>
        <div data-layout="row" data-layout-align="center">
          <RaisedButton 
              href="/api/v1/oauth.redirect?provider=google" 
              secondary={true} 
              target="_self" 
              className="margin-left-0 margin-right-0 margin-top-10 margin-bottom-10" 
              label="Sign in with Google" />
          <span data-flex="5"></span>
          <RaisedButton 
              href="/api/v1/oauth.redirect?provider=github" 
              secondary={true} 
              target="_self" 
              className="margin-left-0 margin-right-0 margin-top-10 margin-bottom-10" 
              label="Sign in with GitHub" />
        </div>

        <form onSubmit={this._submit}>
          <TextField 
              onChange={this._set_email} 
              className="margin-vertical-10" 
              fullWidth={true} 
              floatingLabelText="Email address" 
              errorText={valid.email_error} />
          <TextField 
              onChange={this._set_password} 
              className="margin-vertical-10" 
              fullWidth={true} 
              floatingLabelText="Password" 
              type="password" 
              errorText={valid.password_error} />
          <div data-layout="row" data-layout-align="space-between center" className="margin-vertical-10">
            <div data-flex>
              <Checkbox onCheck={this._set_remember} defaultChecked={this.state.remember} label="Remember Me" />
            </div>
            <div>
              <FlatButton containerElement={<Link to="/app/auth/forgot" />} label="Forgot Password" primary={false}/> 
            </div>
         </div>

          <div className="margin-vertical-10">
            <RaisedButton 
                type="submit" 
                onClick={this._submit} 
                className="full-width" 
                disabled={!valid.ready} 
                label="Log In" primary={true}/> 
          </div>
          <div className="margin-vertical-10">
            <FlatButton 
                containerElement={<Link to="/app/auth/register" />} 
                className="full-width" 
                label="Register your account" 
                primary={true}/> 
          </div>
        </form>
      </AuthBody>
    </AuthBox>
        )
    }
}
```

from actions.js &#8212; what I find interesting is that the best place to save the authentication token is from here.

```javascript
export function loginUser(creds, next) {
    return dispatch => {
        dispatch(requestLogin(creds))

        axios.post('/api/v1/auth.login', {email:creds.email, password:creds.password})
             .then((response) => {
                let resp = response.data
                if (resp.ok) {
                    _saveToken(resp.token, creds.remember)
                    dispatch(receiveLogin(resp.token))
                    browserHistory.push(next ? next : DEFAULT_HOME_PAGE)
                } else {
                    dispatch(loginError(resp.error))
                }
             }).catch((response) => {
                dispatch(loginError("internal error"))
             })
    }
}
```

### Conclusion

There is a big shift in thinking from Angular to React. The biggest is what the state is, this is compounded by using Redux. Where your controller actions are now moved to actions.js and reducer.js.  So far for most of my cases the reducer feels pretty trivial:

```javascript
    case T.LOGIN_SUCCESS:
        return { ...state, 
                 isFetching: true, 
                 isAuthenticated: true, 
                 errorMessage: undefined }
```

It&#8217;s possible to totally understand the route that an application is taking, though it still requires a bit of work to change thinking from all-in-one controller to having the logic spread across three files.

Is this easier to rationalize about a program, maybe, maybe not.  It&#8217;s clear where the state is and that all state changes are initiated in actions.js which can be shared and re-used quickly. Would this be solved if people just designed good programs to start with, probably, but I understand the value of creating these abstractions to force thinking.
