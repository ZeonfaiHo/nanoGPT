# init_from = 'resume'

out_dir = 'out-nano-gpt2-BlockBiLinReGLU-2'
eval_interval = 1000
eval_iters = 500 # number of batches for evaluation
log_interval = 10

always_save_checkpoint = False

wandb_log = False

dataset = 'openwebtext'
# 16k tokens for each weight update
gradient_accumulation_steps = 1
batch_size = 16
block_size = 1024

# baby GPT model :)
n_layer = 6
n_head = 6
n_embd = 384

# learning_rate = 2e-4
# min_lr = 2e-5 # learning_rate / 10 usually
learning_rate = 1e-3
min_lr = 1e-4 # learning_rate / 10 usually
beta2 = 0.99 # make a bit bigger because number of tokens per iter is small

# max_iters = 1e5
max_iters = 2e5
lr_decay_iters = 1e5 # make equal to max_iters usually

warmup_iters = 100
