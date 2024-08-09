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

    // FIXME: For some reason, uncommenting these lines makes compilation fail due to unresolved references
    // Unsure if it is due to them only being available when publishing or what is up?
    //
    // The disassembly of `publishing` specifies that only `channel`, `marketplaceUrl`, `token` and `vendorId`
    // can be specified
//    publishing {
//        licenseUrl = "https://github.com/catppuccin/fleet/blob/main/LICENSE"
//        sourceCodeUrl = "https://github.com/catppuccin/fleet"
//    }
}
