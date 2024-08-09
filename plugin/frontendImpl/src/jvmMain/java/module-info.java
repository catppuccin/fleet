module com.github.catppuccin.fleet {
    requires fleet.frontend;
    requires fleet.kernel;
    requires fleet.util.logging.api;
    requires fleet.rhizomedb;
    requires fleet.frontend.ui;

    exports com.github.catppuccin.fleet;
    provides fleet.kernel.plugins.Plugin with com.github.catppuccin.fleet.CatppuccinTheme;
}
