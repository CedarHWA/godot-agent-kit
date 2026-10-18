> Source: https://docs.godotengine.org/en/4.7/tutorials/export/exporting_for_macos.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="exporting-for-macos"></a>

<a id="doc-exporting-for-macos"></a>

# Exporting for macOS

See also

This page describes how to export a Godot project to macOS.
If you're looking to compile editor or export template binaries from source instead,
read [Compiling for macOS](../../engine_details/development/compiling/compiling_for_macos.md#doc-compiling-for-macos).

macOS apps exported with the official export templates are exported as a single "Universal 2" binary `.app` bundle, a folder with a specific structure which stores the executable, libraries and all the project files.
This bundle can be exported as is, packed in a ZIP archive, or packed in a DMG disk image (only supported when exporting from macOS).
[Universal binaries for macOS support both Intel x86_64 and ARM64 (Apple Silicon) architectures](https://developer.apple.com/documentation/apple-silicon/building-a-universal-macos-binary).

Warning

Due to file system limitations, `.app` bundles exported from Windows lack the
`executable` flag and won't run on macOS. Projects exported as `.zip` are not
affected by this issue. To run `.app` bundles exported from Windows on macOS,
transfer the `.app` to a device running macOS or Linux and use the
`chmod +x {executable_name}` terminal command to add the `executable` permission.
The main executable located in the `Contents/MacOS/` subfolder, as well
as optional helper executables in the `Contents/Helpers/` subfolder, should have
the `executable` permission for the `.app` bundle to be valid.

<a id="requirements"></a>

## Requirements

- Download the Godot export templates. Use the Godot menu: `Editor > Manage Export Templates`.
- A valid and unique `Bundle identifier` should be set in the `Application` section of the export options.

Note

A valid bundle ID can only contain alphanumeric characters, hyphens, and periods (`A-Z`, `a-z`, `0-9`, `-`, and `.`).
Apple recommends using reverse-DNS format (e.g. `com.example.your-game`) of a domain you own, so that your bundle ID is guaranteed to be unique.
Bundle IDs are case-insensitive. See [CFBundleIdentifier](https://developer.apple.com/documentation/bundleresources/information-property-list/cfbundleidentifier).

Warning

Projects exported without code signing and notarization will be blocked by Gatekeeper if they are downloaded from unknown sources, see the [Running Godot apps on macOS](running_on_macos.md#doc-running-on-macos) page for more information.

<a id="code-signing-and-notarization"></a>

## Code signing and notarization

By default, macOS will run only applications that are signed and notarized. If you use any other signing configuration, see [Running Godot apps on macOS](running_on_macos.md#doc-running-on-macos) for workarounds.

To notarize an app, you **must** have a valid [Apple Developer ID Certificate](https://developer.apple.com/).

<a id="if-you-have-an-apple-developer-id-certificate-and-exporting-from-macos"></a>

### If you have an Apple Developer ID Certificate and exporting from macOS

Install [Xcode](https://developer.apple.com/xcode/) command line tools and open Xcode at least once or run the `sudo xcodebuild -license accept` command to accept license agreement.

<a id="to-sign-exported-app"></a>

#### To sign exported app

- Select `Xcode codesign` in the `Code Signing > Codesign` option.
- Set valid Apple ID certificate identity (certificate "Common Name") in the `Code Signing > Identity` section.

<a id="to-notarize-exported-app"></a>

#### To notarize exported app

- Select `Xcode notarytool` in the `Notarization > Notarization` option.
- Disable the `Debugging` entitlement.
- Set valid Apple ID login / app. specific password or [App Store Connect](https://developer.apple.com/documentation/appstoreconnectapi) API UUID / Key in the `Notarization` section.

You can use the `xcrun notarytool history` command to check notarization status and use the `xcrun notarytool log {ID}` command to download the notarization log.

If you encounter notarization issues, see [Resolving common notarization issues](https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution/resolving_common_notarization_issues) for more info.

After notarization is completed, [staple the ticket](https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution/customizing_the_notarization_workflow) to the exported project.

<a id="if-you-have-an-apple-developer-id-certificate-and-exporting-from-linux-or-windows"></a>

### If you have an Apple Developer ID Certificate and exporting from Linux or Windows

Install [rcodesign](https://github.com/indygreg/apple-platform-rs/tree/main/apple-codesign), and configure the path to `rcodesign` in the `Editor Settings > Export > macOS > rcodesign` option.

<a id="id1"></a>

#### To sign exported app

- Select `rcodesign` in the `Code Signing > Codesign` option.
- Set valid Apple ID PKCS #12 certificate file and password in the `Code Signing` section.

<a id="id2"></a>

#### To notarize exported app

- Select `rcodesign` in the `Notarization > Notarization` option.
- Disable the `Debugging` entitlement.
- Set valid [App Store Connect](https://developer.apple.com/documentation/appstoreconnectapi) API UUID / Key in the `Notarization` section.

You can use the `rcodesign notary-log` command to check notarization status.

After notarization is completed, use the `rcodesign staple` command to staple the ticket to the exported project.

<a id="if-you-do-not-have-an-apple-developer-id-certificate"></a>

### If you do not have an Apple Developer ID Certificate

- Select `Built-in (ad-hoc only)` in the `Code Signing > Codesign` option.
- Select `Disabled` in the `Notarization > Notarization` option.

In this case Godot will use an ad-hoc signature, which will make running an exported app easier for the end users,
see the [Running Godot apps on macOS](running_on_macos.md#doc-running-on-macos) page for more information.

<a id="signing-options"></a>

### Signing Options

| Option | Description |
| --- | --- |
| Codesign | Tool to use for code signing. |
| Identity | The "Full Name" or "Common Name" of the signing identity, store in the macOS keychain.  <a id="id3"></a> [[1]](exporting_for_macos.md#id6) |
| Certificate File | The PKCS #12 certificate file.  <a id="id4"></a> [[2]](exporting_for_macos.md#id7) |
| Certificate Password | Password for the certificate file.  <a id="id5"></a> [[2]](exporting_for_macos.md#id7) |
| Custom Options | Array of command line arguments passed to the code signing tool. |

<a id="id6"></a>
[[1](exporting_for_macos.md#id3)]

This option is visible only when signing with Xcode codesign.


<a id="id7"></a>
[2]
([1](exporting_for_macos.md#id4),[2](exporting_for_macos.md#id5))

These options are visible only when signing with rcodesign.

<a id="notarization-options"></a>

### Notarization Options

| Option | Description |
| --- | --- |
| Notarization | Tool to use for notarization. |
| Apple ID Name | Apple ID account name (email address).  <a id="id8"></a> [[3]](exporting_for_macos.md#id11) |
| Apple ID Password | Apple ID app-specific password. See [Using app-specific passwords](https://support.apple.com/en-us/HT204397) to enable two-factor authentication and create app password.  <a id="id9"></a> [[3]](exporting_for_macos.md#id11) |
| Apple Team ID | Team ID ("Organization Unit"), if your Apple ID belongs to multiple teams (optional).  <a id="id10"></a> [[3]](exporting_for_macos.md#id11) |
| API UUID | Apple [App Store Connect](https://developer.apple.com/documentation/appstoreconnectapi) API issuer UUID. |
| API Key | Apple [App Store Connect](https://developer.apple.com/documentation/appstoreconnectapi) API key. |

Note

You should set either Apple ID Name/Password or App Store Connect API UUID/Key.

<a id="id11"></a>
[3]
([1](exporting_for_macos.md#id8),[2](exporting_for_macos.md#id9),[3](exporting_for_macos.md#id10))

These options are visible only when notarizing with Xcode notarytool.

See [Notarizing macOS Software Before Distribution](https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution?language=objc) for more info.

<a id="entitlements"></a>

## Entitlements

<a id="hardened-runtime-entitlements"></a>

### Hardened Runtime Entitlements

Hardened Runtime entitlements manage security options and resource access policy.
See [Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime?language=objc) for more info.

| Entitlement | Description |
| --- | --- |
| Allow JIT Code Execution  <a id="id12"></a> [[4]](exporting_for_macos.md#id20) | Allows creating writable and executable memory for JIT code. If you are using add-ons with dynamic or self-modifying native code, enable them according to the add-on documentation. |
| Allow Unsigned Executable Memory  <a id="id13"></a> [[4]](exporting_for_macos.md#id20) | Allows creating writable and executable memory without JIT restrictions. If you are using add-ons with dynamic or self-modifying native code, enable them according to the add-on documentation. |
| Allow DYLD Environment Variables  <a id="id14"></a> [[4]](exporting_for_macos.md#id20) | Allows app to use dynamic linker environment variables to inject code. If you are using add-ons with dynamic or self-modifying native code, enable them according to the add-on documentation. |
| Disable Library Validation | Allows app to load arbitrary libraries and frameworks. Enable it if you are using GDExtension add-ons or ad-hoc signing, or want to support user-provided external add-ons. |
| Audio Input | Enable if you need to use the microphone or other audio input sources, if it's enabled you should also provide usage message in the privacy/microphone_usage_description option. |
| Camera | Enable if you need to use the camera, if it's enabled you should also provide usage message in the privacy/camera_usage_description option. |
| Location | Enable if you need to use location information from Location Services, if it's enabled you should also provide usage message in the privacy/location_usage_description option. |
| Address Book | <a id="id15"></a> [[5]](exporting_for_macos.md#id21) Enable to allow access contacts in the user's address book, if it's enabled you should also provide usage message in the privacy/address_book_usage_description option. |
| Calendars | <a id="id16"></a> [[5]](exporting_for_macos.md#id21) Enable to allow access to the user's calendar, if it's enabled you should also provide usage message in the privacy/calendar_usage_description option. |
| Photo Library | <a id="id17"></a> [[5]](exporting_for_macos.md#id21) Enable to allow access to the user's Photos library, if it's enabled you should also provide usage message in the privacy/photos_library_usage_description option. |
| Apple Events | <a id="id18"></a> [[5]](exporting_for_macos.md#id21) Enable to allow app to send Apple events to other apps. |
| Debugging | <a id="id19"></a> [[6]](exporting_for_macos.md#id22) You can temporarily enable this entitlement to use native debugger (GDB, LLDB) with the exported app. This entitlement should be disabled for production export. |

<a id="id20"></a>
[4]
([1](exporting_for_macos.md#id12),[2](exporting_for_macos.md#id13),[3](exporting_for_macos.md#id14))

The `Allow JIT Code Execution`, `Allow Unsigned Executable Memory` and `Allow DYLD Environment Variables` entitlements are always enabled for the Godot Mono exports, and are not visible in the export options.


<a id="id21"></a>
[5]
([1](exporting_for_macos.md#id15),[2](exporting_for_macos.md#id16),[3](exporting_for_macos.md#id17),[4](exporting_for_macos.md#id18))

These features aren't supported by Godot out of the box, enable them only if you are using add-ons which require them.


<a id="id22"></a>
[[6](exporting_for_macos.md#id19)]

To notarize an app, you must disable the `Debugging` entitlement.

<a id="app-sandbox-entitlement"></a>

### App Sandbox Entitlement

The App Sandbox restricts access to user data, networking and devices.
Sandboxed apps can't access most of the file system, can't use custom file dialogs and execute binaries (using `OS.execute` and `OS.create_process`) outside the `.app` bundle.
See [App Sandbox](https://developer.apple.com/documentation/security/app_sandbox?language=objc) for more info.

Note

To distribute an app through the App Store, you must enable the App Sandbox.

| Entitlement | Description |
| --- | --- |
| Enabled | Enables App Sandbox. |
| Network Server | Enable to allow app to listen for incoming network connections. |
| Network Client | Enable to allow app to establish outgoing network connections. |
| Device USB | Enable to allow app to interact with USB devices. This entitlement is required to use wired controllers. |
| Device Bluetooth | Enable to allow app to interact with Bluetooth devices. This entitlement is required to use wireless controllers. |
| Files Downloads  <a id="id23"></a> [[7]](exporting_for_macos.md#id28) | Allows read or write access to the user's "Downloads" folder. |
| Files Pictures  <a id="id24"></a> [[7]](exporting_for_macos.md#id28) | Allows read or write access to the user's "Pictures" folder. |
| Files Music  <a id="id25"></a> [[7]](exporting_for_macos.md#id28) | Allows read or write access to the user's "Music" folder. |
| Files Movies  <a id="id26"></a> [[7]](exporting_for_macos.md#id28) | Allows read or write access to the user's "Movies" folder. |
| Files User Selected  <a id="id27"></a> [[7]](exporting_for_macos.md#id28) | Allows read or write access to arbitrary folder. To gain access, a folder must be selected from the native file dialog by the user. |
| Helper Executable | List of helper executables to embedded to the app bundle. Sandboxed app are limited to execute only these executable. |

<a id="id28"></a>
[7]
([1](exporting_for_macos.md#id23),[2](exporting_for_macos.md#id24),[3](exporting_for_macos.md#id25),[4](exporting_for_macos.md#id26),[5](exporting_for_macos.md#id27))

You can optionally provide usage messages for various folders in the privacy/\*_folder_usage_description options.

Note

You can override default entitlements by selecting custom entitlements file, in this case all other entitlement are ignored.

<a id="environment-variables"></a>

## Environment variables

You can use the following environment variables to set export options outside of
the editor. During the export process, these override the values that you set in
the export menu.

<a id="id29"></a>

macOS export environment variables

| Export option | Environment variable |
| --- | --- |
| Encryption / Encryption Key | `GODOT_SCRIPT_ENCRYPTION_KEY` |
| Options / Codesign / Certificate File | `GODOT_MACOS_CODESIGN_CERTIFICATE_FILE` |
| Options / Codesign / Certificate Password | `GODOT_MACOS_CODESIGN_CERTIFICATE_PASSWORD` |
| Options / Codesign / Provisioning Profile | `GODOT_MACOS_CODESIGN_PROVISIONING_PROFILE` |
| Options / Notarization / API UUID | `GODOT_MACOS_NOTARIZATION_API_UUID` |
| Options / Notarization / API Key | `GODOT_MACOS_NOTARIZATION_API_KEY` |
| Options / Notarization / API Key ID | `GODOT_MACOS_NOTARIZATION_API_KEY_ID` |
| Options / Notarization / Apple ID Name | `GODOT_MACOS_NOTARIZATION_APPLE_ID_NAME` |
| Options / Notarization / Apple ID Password | `GODOT_MACOS_NOTARIZATION_APPLE_ID_PASSWORD` |

<a id="export-options"></a>

## Export options

You can find a full list of export options available in the
[EditorExportPlatformMacOS](../../classes/class_editorexportplatformmacos.md#class-editorexportplatformmacos) class reference.
