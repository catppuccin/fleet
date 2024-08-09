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

    publishing {
        // https://github.com/JetBrains/fleet-theme-plugin-template/issues/2#issuecomment-2278303755
        // 29aa2a92-b107-4388-8ea5-39636c6cce03 is the ID of @sgoudham
        vendorId = "29aa2a92-b107-4388-8ea5-39636c6cce03"
    }
}
