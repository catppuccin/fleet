package com.github.catppuccin.fleet

import fleet.dock.api.ThemeId
import fleet.frontend.theme.registerTheme
import fleet.kernel.plugins.ContributionScope
import fleet.kernel.plugins.Plugin
import fleet.kernel.plugins.PluginScope

class CatppuccinTheme : Plugin<Unit> {
    companion object : Plugin.Key<Unit>

    override val key: Plugin.Key<Unit> = CatppuccinTheme

    override fun ContributionScope.load(pluginScope: PluginScope) {
        registerTheme(ThemeId(id = "catppuccin-frappe"))
        registerTheme(ThemeId(id = "catppuccin-macchiato"))
        registerTheme(ThemeId(id = "catppuccin-mocha"))
        registerTheme(ThemeId(id = "catppuccin-latte"))
    }
}
