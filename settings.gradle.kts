rootProject.name = "Catppuccin Fleet Theme"

include(":plugin")
include(":plugin:frontendImpl")

pluginManagement {
    repositories {
        mavenCentral()
        gradlePluginPortal()
        maven("https://cache-redirector.jetbrains.com/intellij-dependencies")
        maven("https://packages.jetbrains.team/maven/p/fleet/fleet-sdk")
    }
}
