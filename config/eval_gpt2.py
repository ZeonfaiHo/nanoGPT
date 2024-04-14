# evaluate the base gpt2
# n_layer=12, n_head=12, n_embd=768
# 124M parameters
batch_size = 8
eval_iters = 500
block_size = 1024

eval_only = True
wandb_log = False
init_from = 'resume'
out_dir = 'out-gpt2-BlockReGLU'
