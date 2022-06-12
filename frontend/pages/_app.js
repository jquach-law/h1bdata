import { QueryClient, QueryClientProvider } from "react-query";
import { Provider } from "react-redux";
import "../styles/global.css";
import store from "../state/store";

const queryClient = new QueryClient();

export default function App({ Component, pageProps }) {
  return (
    <QueryClientProvider client={queryClient}>
      <Provider store={store}>
        <Component {...pageProps} />;
      </Provider>
    </QueryClientProvider>
  );
}
