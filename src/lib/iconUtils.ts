import { Home, SettingConfig, setConfig, SettingTwo } from "@icon-park/svg";

setConfig({
  size: "1.5em",
  strokeWidth: 4,
  strokeLinecap: "butt",
  strokeLinejoin: "round",
  prefix: "",
  theme: "filled",
  colors: {
    outline: {
      fill: "#333",
      background: "#fff",
    },
    filled: {
      fill: "#333",
      background: "#fff",
    },
    twoTone: {
      fill: "",
      twoTone: "",
    },
    multiColor: {
      outStrokeColor: "",
      outFillColor: "",
      innerStrokeColor: "",
      innerFillColor: "",
    },
  },
});

function getIcon(which: string, pathname: string) {
  if (which === "home") {
    const theme = pathname === "/" ? "filled" : "outline";
    return Home({
      theme,
    });
  } else if (which === "setting-two") {
    const theme = pathname === "/settings" ? "filled" : "outline";
    return SettingTwo({ theme });
  }
}

export { getIcon };
