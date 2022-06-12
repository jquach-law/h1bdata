import { combineReducers } from "redux";

import searchReducer from "./slices/searchSlice";

export default combineReducers({
  searchSlice: searchReducer,
});
