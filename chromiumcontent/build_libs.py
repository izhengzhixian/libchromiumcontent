import argparse
import os
import subprocess
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-o', dest='out')
parser.add_argument('-s', dest='stamp')
parser.add_argument('-t', dest='target_cpu')
args = parser.parse_args()

def walk_dir(root, exclude_dirs=[]):
    for dir, subdirs, files in os.walk(root):
        for exclude_dir in exclude_dirs:
            test_dir = os.path.join(*(dir.split(os.path.sep)[1:]))
            if exclude_dirs and test_dir in exclude_dirs:
                files = []
        yield dir, subdirs, files

def gen_list(out, name, obj_dirs, exclude_dirs=[]):
    out.write(name + " = [\n")
    for base_dir in obj_dirs:
        base_path = os.path.join('obj', base_dir)
        for dir, subdirs, files in walk_dir(base_path, exclude_dirs):
            for f in files:
                if f.endswith('.obj') or f.endswith('.o'):
                    out.write('"' + os.path.abspath(os.path.join(dir, f)) + '",\n')
    out.write("]\n")

with open(args.out, 'w') as out:
    additional_libchromiumcontent = []
    if sys.platform in ['win32', 'cygwin'] and args.target_cpu == "x64":
        additional_libchromiumcontent = [
            "../win_clang_x64/obj/third_party/libyuv",
        ]

    gen_list(
        out,
        "obj_libchromiumcontent",
        [
            "build",
            "chrome/browser/ui/libgtkui",
            "content",
            "crypto",
            "dbus",
            "device",
            "gin",
            "google_apis",
            "gpu",
            "ipc",
            "jingle",
            "mojo",
            "pdf",
            "printing",
            "sandbox",
            "sdch",
            "sql/sql",
            "storage",
            "third_party/adobe",
            "third_party/boringssl",
            "third_party/brotli/common",
            "third_party/brotli/dec",
            "third_party/ced/ced",
            "third_party/crc32c",  # for "third_party/leveldatabase"
            "third_party/decklink",
            "third_party/expat",
            "third_party/flac",
            "third_party/harfbuzz-ng",
            "third_party/iaccessible2",
            "third_party/iccjpeg",
            "third_party/isimpledom",
            "third_party/leveldatabase",
            "third_party/libdrm",
            "third_party/libXNVCtrl",
            "third_party/libjingle",
            "third_party/libjpeg_turbo",
            "third_party/libpng",
            "third_party/libsrtp",
            "third_party/libusb",
            "third_party/libvpx",
            "third_party/libwebm",
            "third_party/libwebp",
            "third_party/libxml",
            "third_party/libxslt",
            "third_party/libyuv",
            "third_party/mesa",
            "third_party/modp_b64",
            "third_party/mozilla",
            "third_party/openh264",
            "third_party/openmax_dl",
            "third_party/opus",
            "third_party/ots",
            "third_party/protobuf/protobuf_lite",
            "third_party/qcms",
            "third_party/re2",
            "third_party/sfntly",
            "third_party/smhasher",
            "third_party/snappy",
            "third_party/sqlite",
            "third_party/sudden_motion_sensor",
            "third_party/usrsctp",
            "third_party/woff2",
            "third_party/zlib",
            "tools",
            "ui",
            "url",
        ] + additional_libchromiumcontent,
        [
            "tools/v8_context_snapshot/v8_context_snapshot_generator"
        ])

    gen_list(
        out,
        "obj_libcxx",
        [
            "buildtools/third_party/libc++",
            "buildtools/third_party/libc++abi",
        ])

    gen_list(
        out,
        "obj_base",
        [
            "base",
        ])

    gen_list(
        out,
        "obj_cc",
        [
            "cc/animation",
            "cc/base",
            "cc/blink",
            "cc/cc",
            "cc/debug",
            "cc/ipc",
            "cc/paint",
            "cc/proto",
            "cc/surfaces",
        ])

    gen_list(
        out,
        "obj_components",
        [
            "components/autofill/core/common",
            "components/bitmap_uploader",
            "components/cbor",
            "components/cdm",
            "components/cookie_config",
            "components/crash/core/common",
            "components/data_reduction_proxy/core/common",
            "components/device_event_log",
            "components/discardable_memory",
            "components/display_compositor",
            "components/download",
            "components/filename_generation",
            "components/filesystem",
            "components/leveldb",
            "components/leveldb_proto",
            "components/link_header_util",
            "components/memory_coordinator",
            "components/metrics/public/interfaces",
            "components/metrics/single_sample_metrics",
            "components/mime_util",
            "components/mus/clipboard",
            "components/mus/common",
            "components/mus/gles2",
            "components/mus/gpu",
            "components/mus/input_devices",
            "components/mus/public",
            "components/net_log",
            "components/network_session_configurator",
            "components/os_crypt",
            "components/password_manager/core/common",
            "components/payments",
            "components/prefs",
            "components/proxy_config",
            "components/rappor",
            "components/scheduler/common",
            "components/scheduler/scheduler",
            "components/security_state",
            "components/tracing/proto",
            "components/tracing/startup_tracing",
            "components/tracing/tracing",
            "components/url_formatter",
            "components/variations",
            "components/vector_icons",
            "components/version_info",
            "components/viz/client",
            "components/viz/common",
            "components/viz/hit_test",
            "components/viz/host",
            "components/viz/service",
            "components/webcrypto",
            "components/webmessaging",
        ])

    gen_list(
        out,
        "obj_ppapi",
        [
            "ppapi/cpp/objects",
            "ppapi/cpp/private",
            "ppapi/host",
            "ppapi/proxy",
            "ppapi/shared_impl",
            "ppapi/thunk",
        ])

    gen_list(
        out,
        "obj_media",
        [
            "media",
            "third_party/libaom",
        ])

    gen_list(
        out,
        "obj_net",
        [
            "net/base",
            "net/constants",
            "net/dns",
            "net/extras",
            "net/interfaces",
            "net/http_server",
            "net/net",
            "net/net_browser_services",
            "net/net_utility_services",
            "net/net_with_v8",
            "net/proxy_resolution",
            "net/net_nqe_proto",
        ])

    gen_list(
        out,
        "obj_services",
        [
            "services/audio",
            "services/catalog",
            "services/data_decoder",
            "services/device",
            "services/file",
            "services/metrics",
            "services/network",
            "services/proxy_resolver",
            "services/resource_coordinator",
            "services/service_manager",
            "services/shape_detection",
            "services/shell/public",
            "services/shell/runner",
            "services/shell/shell",
            "services/tracing",
            "services/ui/public",
            "services/ui/gpu",
            "services/user",
            "services/video_capture",
            "services/viz",
        ])

    gen_list(
        out,
        "obj_skia",
        [
            "skia",
        ])

    gen_list(
        out,
        "obj_angle",
        [
            "third_party/angle/angle_common",
            "third_party/angle/angle_gpu_info_util",
            "third_party/angle/angle_image_util",
            "third_party/angle/libANGLE",
            "third_party/angle/libEGL",
            "third_party/angle/libGLESv2",
            "third_party/angle/preprocessor",
            "third_party/angle/src/third_party/libXNVCtrl",
            "third_party/angle/third_party/glslang",
            "third_party/angle/third_party/vulkan-validation-layers/vulkan_loader",
            "third_party/angle/translator",
            "third_party/angle/translator_lib",
        ])

    gen_list(
        out,
        "obj_pdfium",
        [
            "third_party/freetype",
            "third_party/pdfium",
        ])

    gen_list(
        out,
        "obj_blink",
        [
            "third_party/blink/common",
            "third_party/blink/public",
            "third_party/blink/renderer/controller",
            "third_party/blink/renderer/platform",
            "third_party/blink/renderer/web",
        ],
        [
            "third_party/blink/renderer/platform/character_data_generator"
        ])

    gen_list(
        out,
        "obj_blinkcore",
        [
            "third_party/blink/renderer/core",
        ])

    gen_list(
        out,
        "obj_blinkbindings",
        [
            "third_party/blink/renderer/bindings",
        ])

    gen_list(
        out,
        "obj_blinkmodules",
        [
            "third_party/blink/renderer/modules",
        ])

    gen_list(
        out,
        "obj_v8",
        [
            "v8/src/inspector",
            "v8/v8_external_snapshot",
            "v8/v8_libbase",
            "v8/v8_libplatform",
            "v8/v8_libsampler",
            "third_party/icu",
        ])

open(args.stamp, 'w')
