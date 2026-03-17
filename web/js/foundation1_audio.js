import { app } from "../../../scripts/app.js";
import { api } from "../../../scripts/api.js";

app.registerExtension({
    name: "SCG.Foundation1.AudioPreview",

    async beforeRegisterNodeDef(nodeType, nodeData, _app) {
        if (nodeData.name !== "SCGFoundation1Sampler") {
            return;
        }

        const origOnNodeCreated = nodeType.prototype.onNodeCreated;
        nodeType.prototype.onNodeCreated = function () {
            if (origOnNodeCreated) {
                origOnNodeCreated.apply(this, arguments);
            }

            const audioEl = document.createElement("audio");
            audioEl.controls = true;
            audioEl.style.width = "100%";

            const audioWidget = this.addDOMWidget(
                "audio_preview", "audio", audioEl,
                { serialize: false, hideOnZoom: false }
            );
            audioWidget.computeSize = function (width) {
                return [width, 54];
            };

            this.audioElement = audioEl;
            this.audioWidget = audioWidget;
        };

        const origOnExecuted = nodeType.prototype.onExecuted;
        nodeType.prototype.onExecuted = function (message) {
            if (origOnExecuted) {
                origOnExecuted.apply(this, arguments);
            }

            if (!message || !message.audio || message.audio.length === 0) return;

            const info = message.audio[0];
            const params = new URLSearchParams({
                filename: info.filename,
                subfolder: info.subfolder || "",
                type: info.type || "temp",
            });
            const url = api.apiURL(`/view?${params.toString()}`);

            if (this.audioElement) {
                this.audioElement.src = url;
                this.audioElement.load();
                if (info.autoplay) {
                    this.audioElement.play().catch(() => {});
                }
            }
        };
    },
});
