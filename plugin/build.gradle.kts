plugins {
    base
    alias(libs.plugins.fleet.plugin)
}

version = "0.1.0"

fleetPlugin {
    id = "com.github.catppuccin.fleet"

    metadata {
        readableName = "Catppuccin Fleet Theme"
        description = "🌊 Soothing pastel theme for JetBrains Fleet"

        icons {
            default.set(project.layout.projectDirectory.file("pluginIcon.svg"))
            dark.set(project.layout.projectDirectory.file("pluginIcon.svg"))
        }
    }

    fleetRuntime {
        version = libs.versions.fleet.runtime
    }
}
