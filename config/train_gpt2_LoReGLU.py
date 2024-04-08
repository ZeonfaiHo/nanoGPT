init_from = 'resume'
out_dir = 'out-gpt2-LoReGLU'

wandb_log = False

always_save_checkpoint = False

# these make the total batch size be ~0.5M
# 12 batch size * 1024 block size * 5 gradaccum * 8 GPUs = 491,520
batch_size = 8
block_size = 1024
gradient_accumulation_steps = 60

learning_rate = 5e-4 # max learning rate
min_lr = 5e-5 # minimum learning rate, should be ~= learning_rate/10 per Chinchilla

# this makes total number of tokens be 300B
max_iters = 600000
lr_decay_iters = 600000

# eval stuff
eval_interval = 500
eval_iters = 200
log_interval = 10

# weight decay
weight_decay = 1e-1
