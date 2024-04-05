gradient_accumulation_steps = 1
batch_size = 16
block_size = 1024

eval_iters = 1000 # use more iterations to get good estimate

compile = True
eval_only = True
wandb_log = False
init_from = 'resume'
out_dir = 'out-nano-gpt2-LoReGLU'

