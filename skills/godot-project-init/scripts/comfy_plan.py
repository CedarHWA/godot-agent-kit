"""Generate a fresh project WAI graph, with API and editable LiteGraph representations."""
import json


def baseline(model):
    nodes = {
        "1": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": model["destination"].split("/")[-1]}},
        "2": {"class_type": "CLIPSetLastLayer", "inputs": {"clip": ["1", 1], "stop_at_clip_layer": -2}},
        "3": {"class_type": "CLIPTextEncode", "inputs": {"text": "masterpiece, best quality, anime illustration, 1girl, adult woman, solo, blue jacket, short brown hair, neutral background, upper body", "clip": ["2", 0]}},
        "4": {"class_type": "CLIPTextEncode", "inputs": {"text": "worst quality, low quality, lowres, bad anatomy, bad hands, text, watermark", "clip": ["2", 0]}},
        "5": {"class_type": "EmptyLatentImage", "inputs": {"width": 1024, "height": 1024, "batch_size": 1}},
        "6": {"class_type": "KSampler", "inputs": {"model": ["1", 0], "positive": ["3", 0], "negative": ["4", 0], "latent_image": ["5", 0], "seed": 1, "steps": 28, "cfg": 5.5, "sampler_name": "euler_ancestral", "scheduler": "normal", "denoise": 1.0}},
        "7": {"class_type": "VAEDecode", "inputs": {"samples": ["6", 0], "vae": ["1", 2]}},
        "8": {"class_type": "SaveImage", "inputs": {"images": ["7", 0], "filename_prefix": "wai/baseline"}},
    }
    # Node socket order is explicit; widget values follow the built-in node schemas.
    spec = {
        "1": ([], [("MODEL", "MODEL"), ("CLIP", "CLIP"), ("VAE", "VAE")], [nodes["1"]["inputs"]["ckpt_name"]], [40, 300]),
        "2": ([("clip", "CLIP")], [("CLIP", "CLIP")], [-2], [400, 200]),
        "3": ([("clip", "CLIP")], [("CONDITIONING", "CONDITIONING")], [nodes["3"]["inputs"]["text"]], [750, 80]),
        "4": ([("clip", "CLIP")], [("CONDITIONING", "CONDITIONING")], [nodes["4"]["inputs"]["text"]], [750, 340]),
        "5": ([], [("LATENT", "LATENT")], [1024, 1024, 1], [750, 610]),
        "6": ([("model", "MODEL"), ("positive", "CONDITIONING"), ("negative", "CONDITIONING"), ("latent_image", "LATENT")], [("LATENT", "LATENT")], [1, "fixed", 28, 5.5, "euler_ancestral", "normal", 1.0], [1120, 200]),
        "7": ([("samples", "LATENT"), ("vae", "VAE")], [("IMAGE", "IMAGE")], [], [1500, 240]),
        "8": ([("images", "IMAGE")], [], ["wai/baseline"], [1850, 240]),
    }
    ui_nodes, links = {}, []
    for key, (inputs, outputs, widgets, pos) in spec.items():
        kind = nodes[key]["class_type"]
        ui_nodes[key] = {"id": int(key), "type": kind, "pos": pos,
                         "size": [320, 240 if key in ("3", "4", "8") else 200],
                         "flags": {}, "order": int(key) - 1, "mode": 0,
                         "inputs": [{"name": n, "type": t, "link": None} for n, t in inputs],
                         "outputs": [{"name": n, "type": t, "links": [], "slot_index": i} for i, (n, t) in enumerate(outputs)],
                         "properties": {"Node name for S&R": kind}, "widgets_values": widgets}
    for key, (inputs, _, _, _) in spec.items():
        for slot, (name, kind) in enumerate(inputs):
            origin, origin_slot = nodes[key]["inputs"][name]
            link = len(links) + 1
            links.append([link, int(origin), origin_slot, int(key), slot, kind])
            ui_nodes[key]["inputs"][slot]["link"] = link
            ui_nodes[origin]["outputs"][origin_slot]["links"].append(link)
    ui = {"last_node_id": 8, "last_link_id": len(links), "nodes": list(ui_nodes.values()),
          "links": links, "groups": [], "config": {}, "extra": {}, "version": 0.4}
    encode = lambda value: (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    return {"tools/comfyui/workflows/wai-t2i.api.json": encode(nodes),
            "tools/comfyui/workflows/wai-t2i.ui.json": encode(ui)}
