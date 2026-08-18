[app]

title = Jarvis AI

package.name = jarvis

package.domain = org.jarvis

source.dir = .

source.include_exts = py,png,jpg,kv,json

version = 1.0

requirements = python3,kivy,requests

orientation = portrait

fullscreen = 0


# Android

android.api = 35

android.minapi = 24

android.archs = arm64-v8a

android.accept_sdk_license = True

android.build_tools_version = 35.0.0

android.allow_backup = True


[buildozer]

log_level = 2

warn_on_root = 1
