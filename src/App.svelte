<script lang="ts">
  import { Route, Router } from "svelte-navigator";
  import Layout from "./components/Layout.svelte";
  import Home from "./routes/Home.svelte";
  import SettingsPage from "./routes/SettingsPage.svelte";
</script>

<Router>
  <Layout>
    <Route path="/" primary={false}>
      <Home />
    </Route>
    <Route path="settings" component={SettingsPage} primary={false} />
  </Layout>
</Router>
