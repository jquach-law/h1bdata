import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  results: [],
};

export const searchSlice = createSlice({
  name: "search",
  initialState,
  reducers: {
    saveSearch: (state, action) => {
      state.results = action.payload;
    },
  },
});

export const { saveSearch } = searchSlice.actions;

export const selectSearchResults = (state) => state.searchSlice.results;

export default searchSlice.reducer;
