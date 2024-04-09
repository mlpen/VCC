# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
from src.args import Args, Options, import_config
import os

__common = import_config(os.path.join(os.path.dirname(os.path.realpath(__file__)), "common.py"))
seed = __common.seed
output_dir = __common.output_dir
save_top_k = __common.save_top_k
project = __common.project
trainer = __common.trainer
optimizer = __common.optimizer
data = __common.data
data.collator_args.max_encoder_length = 4096
optimizer.batch_size = optimizer.batch_size // 4

model = Args()
model.pl_module = "src.t5.tasks.downstream.DownstreamModelModule"
model.model_type = "transformers.T5ForConditionalGeneration"
model.pretrained_config = "t5-large"
model.load_pretrain = {
    "model_type":"transformers.T5ForConditionalGeneration",
    "checkpoint":"t5-large"
}
model.max_decoder_length = data.collator_args.max_decoder_length
model.gradient_checkpointing = False
