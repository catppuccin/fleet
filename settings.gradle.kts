rootProject.name = "Catppuccin Fleet Theme"

include(":catppuccin-theme")
include(":catppuccin-theme:frontendImpl")

pluginManagement {
    repositories {
        mavenCentral()
        gradlePluginPortal()
        maven("https://cache-redirector.jetbrains.com/intellij-dependencies")
        maven("https://packages.jetbrains.team/maven/p/fleet/fleet-sdk")
    }
}
