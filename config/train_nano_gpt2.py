init_from = 'resume'

out_dir = 'out-nano-gpt2-ReGLU'
eval_interval = 2000
eval_iters = 200 # number of batches for evaluation
log_interval = 10

always_save_checkpoint = False

wandb_log = False
wandb_project = 'owt'
wandb_run_name = 'nano-gpt2'

dataset = 'openwebtext'
# 16k tokens for each weight update
gradient_accumulation_steps = 1
batch_size = 16
block_size = 1024

# baby GPT model :)
n_layer = 6
n_head = 6
n_embd = 384

learning_rate = 2e-4
min_lr = 2e-5 # learning_rate / 10 usually
# learning_rate = 1e-3
# min_lr = 1e-4 # learning_rate / 10 usually

# max_iters = 1e5
max_iters = 2e5
lr_decay_iters = 1e5 # make equal to max_iters usually

warmup_iters = 100
