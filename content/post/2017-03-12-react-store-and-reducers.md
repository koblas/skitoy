---
title: React Store and Reducers
author: koblas
layout: post
date: 2017-03-12T19:42:05+00:00
url: /p/react-store-and-reducers/637
categories:
  - react
  - development

---

# React Store and Reducers


Writing a react and redux appliction is a great experience, we all have seen the vision of great applications. However every time you sit down to work on your application there are times that the boilerplate is killing you. In most Redux applications you start seeing it very quickly, since there are great initial demos of "Todo" or other classic applications.

The question is how to create great patterns that scale, rather than great demos that give a flavor.

### Backstory

I have been writing software for many years and playing on my own time with React and Redux. I walked into a project that had a medium sized application already written in React/Redux. Usually that would be a great thing, since you can take the at-home experiences that you have and learn from others. In this case it was an application built by contractors who hadn't ever built a React/Redux application before. It's still a great chance to learn, since different people have different tricks, but it also presents some interesting challenges.

#### What did I find

What was the ugly? You know there was quite a few things, here's a short list of what I needed to do and clean up.

1. **Establish eslint standards** - Used the AirBnB set, it's solid and functional. The code style with about 6 different people working on it was all over the board and made it hard to quickly understand what was happening when you opened a file. Lets just say when it first ran it pulled over 12,000 errors (hint: eslint --fix is your friend to reduce it to 4,000).
2. **Cut-n-paste components** - Well over half of the components were copies of other components with imports that weren't used, methods that never were accessed and other cruft.
2. **Create actions for Redux** - The system only had two actions "load" and "notify" the `loadStore()` action looked like a huge switch statement of these. There was a fleet of reducers on the other side, but every other request that wasn't fetch blob of data was an XHR style request in the React components.

	```
    case "team":
      return (dispatch, getState) => {
        dispatch(requestTeam());
        request.send(
            '/v1/team-members',
            'GET',
            (err, res, param) => {
              dispatch({
                type: 'RECEIVE_TEAM',
                team: res.body,
              });
            },
            null,
            options,
          );
	```
	
3. **No prop validation** - Yeah, you're expecting that after having no linting standards. Adding those takes time, but it makes the documentation of components self evident.
4. **External form models** - There was a really cool idea of having all of the models specified by JSON files that would be fetched from the server to generate forms. It worked and was interesting, the challenge was that it ment every form render had to do a server round trip just to fetch the data. While these could have been imported, it's easier just to build out a `Form` component design pattern. This global form component only knew how to XHR back to the server to GET/POST/PUT payloads.  This is tying the FORM too closely to the API and the API team had to design for the UI (custom endpoints).
4. **The love of state** - Most components in the system used the following pattern, rather than just leaving things in props. Yes, it was much worse than this in many cases.

    ```
    componentWillReceiveProps(nextProps) {
      this.setState({
         data: nextProps.data,
      })
    }
    ```
5. **Constants in state** - Not only is the state loved, but it so loved it has everything you need. Can we say clutter.

    ```
    this.state = {
      data: {
        total: {},
        GatewayTotal: {},
      },
      columnLabels: [
        { label: "Method", value: 'method' },
        { label: "# Payments", value: 'count' },
        { label: "Value", columnClass: "u-right-align", value: 'value', func: "currency" },
      ],
    };

    ```

#### Structuring Redux Stores

The clear thing to do was estiblish read redux actions that supported the API endpoints and moved the React application back to view oriented rendering. The challenge is how to build a great redux design for an existing appliction, since large application redux designing isn't a hotly dicussed topic this is what I did.

Some observations:

1. There are three primary data pools in an application.
    * Individual objects - The objects themselves.
    * List of objects - List results (searches, etc.)
    * Auth/Session/Notifications - Application state
2. Caching is important.
3. Boilerplate is bad... We've all written the same reducer with the names changed, over and over again.

### Basic store design

I recently read this blog post about [twitters redux store](https://medium.com/statuscode/dissecting-twitters-redux-store-d7280b62c6b1). It did present a few interesting ideas, which I adopted. The design of your store is more important than you think, since it's how you're going to structure the application.

```
fetchStatus: ENUM{
  undefined,
  'loading'
  'loaded'
  'error'
}

storeData: {
   entities: { ID: Object },
   fetchStatus: { ID: fetchStatus },
   errors: { ID: Object },
}
```


### Caching Redux Data V1

When you Google around for this question, you'll find lots of articles that avoid talking about it. Since your store should be stateless. You're going to need to cache data to have an efficent application and the store is a good representation of the state of your application which you will be communicating out to your user. Instead of not talking about it, lets do it...

The start of this `loadRecipient()` we check to see the state of the store.

```
export function loadRecipient(id, force) {
  const { entities } = store.getState();
  const data = entities.recipient;

  return (dispatch) => {
    if (!force && (data.fetchStatus[id] === 'loaded' || data.fetchStatus[id] === 'loading')) {
      return;
    }

    if (data.fetchStatus[id] !== 'loaded') {
      dispatch({
        type: RECIPIENT_LOADING,
        loading: "loading",
        id,
      });
    }

    request.GET(`/v1/recipients/${id}`).then(([res, err]) => {
```

The key things to see here are:

1. We return a no-op action in the event that we've already fetched the data. Since your pattern in the Component is `dispatch(loadRecipient(id))`, since you always dispatch you have to return a valid action `undefined` will just crash your application.
2. We set the `loading` state to allow both future requests and the UI to indicate data is coming.
2. We of use a thunk middleware, so we can do an async fetch and get a result back later.

### Basic Reducer V1

Reducers, this is the number one source of boilerplate in most Redux applications. For the moment the application is saving all of the data in the "store.entities" component. The big thing is that while we use "tokens" for our actions and the state, we're also taking advantage that we know that they're really strings and taking advantage of well structured strings to perform the operations that we need.


```
export default function entities(state = initialState, action) {
  if (!action.type.startsWith('entities/')) {
    return state;
  }

  const parts = action.type.split('/');

  if (parts.length !== 3) {
    return state;
  }

  const type = parts[1];
  const opcode = parts[2];
  const id = action.id || 'data';

  if (opcode === 'LOADING') {
    return state.setIn([type, 'fetchStatus', id], action.loading || 'loading');
  } else if (opcode === 'ERROR') {
    return state
             .setIn([type, 'fetchStatus', id], 'error')
             .setIn([type, 'errors', id], action.error);
  } else if (opcode === 'DATA') {
    return state
             .setIn([type, 'fetchStatus', id], 'loaded')
             .setIn([type, 'entities', id], action.data);
  }

  return state;
}
```

## Always be improving 

We we have a basic pattern for our actions and a basic pattern for reducers. The problem is that way too much is now stored in level deeper than we really wish.  How can we improve it but not create more boilerplate.

JavaScript is also a great templating language. We can quickly whip up this reducer generator.

```
import Immutable from 'seamless-immutable';

/*
 * Standard reducer definition
 *
 * It assumes that all actions are of type NAME/OPCODE
 *
 * where name is the name that you registered when you added this to the reducer pipeline
 *
 * e.g.
 *     ...
 *     payments: standardReducer('payments')
 *     ...
 *
 * It assumes all action.types will have the form 'name/OPCODE' where OPCODE is one of:
 *
 *    LOADING -- Mark the fetchStatus as 'loading'
 *    ERROR -- Mark fetch status as 'error' and save the code in error[id]
 *    DATA -- Save the object in the data table and set fetchStatus = 'loaded'
 */
export default function standardReducer(name, extra) {
  const initialState = Immutable({
    entities: {},
    errors: {},
    fetchStatus: {},
  });

  return (state = initialState, action) => {
    if (!action.type.startsWith(`${name}/`)) {
      return state;
    }

    const parts = action.type.split('/');

    if (parts.length === 1) {
      return state;
    }

    const opcode = parts[parts.length - 1];
    const id = action.id || 'data';

    if (opcode === 'LOADING') {
      return state.setIn(['fetchStatus', id], action.loading || 'loading');
    } else if (opcode === 'ERROR') {
      return state
               .setIn(['fetchStatus', id], 'error')
               .setIn(['errors', id], action.error);
    } else if (opcode === 'DATA') {
      return state
               .setIn(['fetchStatus', id], 'loaded')
               .setIn(['entities', id], action.data);
    } else if (extra) {
      return extra(state, action);
    }

    return state;
  };
}
```

The good, we now can add reducers to our system like this, we can even quickly extend a basic reducer with additional action handlers.

```javascript
const rootReducer = combineReducers({
  activity: standardReducer('activity'),
  batchSummary: standardReducer('batchSummary'),
  recipientUpload: standardReducer('recipientUpload', recipientUploadMethods),
});
```

If we need to add some extra reducer functions beyond a basic load function it's easy:

```
import { RECIPIENT_UPLOAD_PROCESSING_START } from '../actions/recipientUpload';

export default function batchUploadMethods(state, action) {
  if (action.type === RECIPIENT_UPLOAD_PROCESSING_START) {
    return state.setIn(['entities', action.id, 'status'], "processing");
  }
  return state;
}
```





