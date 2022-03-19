<script lang="ts">
  import { Route, Router } from "svelte-navigator";
  import Layout from "./components/Layout.svelte";
  import AboutPage from "./routes/AboutPage.svelte";
  import Home from "./routes/Home.svelte";
  import SettingsPage from "./routes/SettingsPage.svelte";
</script>

<Router>
  <Layout>
    <Route path="/" primary={false}>
      <Home />
    </Route>
    <Route path="about" primary={false}>
      <AboutPage />
    </Route>
    <Route path="settings" primary={false}>
      <SettingsPage />
    </Route>
  </Layout>
</Router>
