# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
from src.args import Args

seed = 111111
output_dir = "../outputs"
save_top_k = 50
project = "vcc"

model = Args()
model.pl_module = "src.roberta.tasks.mlm.MLMModelModule"
model.encoder_type = "src.roberta.models.prenorm.PrenormRobertaModel"
model.initializer_range = 0.02
model.vocab_size = 50265
model.type_vocab_size = 1
model.pad_token_id = 1
model.num_hidden_layers = 24
model.num_attention_heads = 16
model.layer_norm_eps = 1e-05
model.intermediate_size = 4096
model.hidden_size = 1024
model.hidden_dropout_prob = 0.1
model.attention_probs_dropout_prob = 0.1
model.max_position_embeddings = 512

trainer = Args()
trainer.strategy = "ddp"
trainer.gradient_clip_val = 1.0
trainer.gpus = 8
trainer.precision = 16
trainer.max_steps = 750000

data = Args()
data.pl_module = "src.roberta.data.data_module_pretrain.PretrainDataModule"
data.num_workers = 8
data.training_dataset_path = "/nobackup/zhanpeng/wiki_en_1k/train.arrow"
data.validation_dataset_path = "/nobackup/zhanpeng/wiki_en_1k/val.arrow"
data.tokenizer = "roberta-base"
data.collator = "src.roberta.data.pretrain.mlm.MLMCollator"
data.collator_args = Args()
data.collator_args.num_masked_tokens = 77
data.collator_args.max_sequence_length = 512

optimizer = Args()
optimizer.optimizer = "adam"
optimizer.adam_beta1 = 0.9
optimizer.adam_beta2 = 0.98
optimizer.adam_epsilon = 1e-6
optimizer.batch_size = 32
optimizer.weight_decay = 0.01
optimizer.base_learning_rate = 1e-3
optimizer.min_lr_ratio = 0.001
optimizer.lr_scheduler_type = "linear"
optimizer.warmup_steps = 2000
