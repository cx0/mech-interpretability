# %%
# change HF cache directory to persist runpod storage
import os
os.environ["TRANSFORMERS_CACHE"] = "/workspace/cache/"

# %%
import torch
import transformer_lens.utils as utils
from transformer_lens import HookedTransformer

# %%
# inference experiments: be frugal and save GPU memory
torch.set_grad_enabled(False)

# %%
device: torch.device = utils.get_device()

# %%
# small models (and CRFM medium variants) available in TransformerLens package
models = ["gpt2-small", "facebook/opt-125m", "EleutherAI/gpt-neo-125M",
          "stanford-crfm/alias-gpt2-small-x21",
          "stanford-crfm/battlestar-gpt2-small-x49",
          "stanford-crfm/caprica-gpt2-small-x81",
          "stanford-crfm/darkmatter-gpt2-small-x343",
          "stanford-crfm/expanse-gpt2-small-x777",
          "stanford-crfm/arwen-gpt2-medium-x21",
          "stanford-crfm/beren-gpt2-medium-x49",
          "stanford-crfm/celebrimbor-gpt2-medium-x81",
          "stanford-crfm/durin-gpt2-medium-x343",
          "stanford-crfm/eowyn-gpt2-medium-x777"]

models_detailed = ["stanford-crfm/alias-gpt2-small-x21",
                   "stanford-crfm/battlestar-gpt2-small-x49",
                   "stanford-crfm/caprica-gpt2-small-x81"]

# checkpoints for Stanford CRFM models
STANFORD_CRFM_CHECKPOINTS = (
    list(range(0, 100, 10))
    + list(range(100, 2000, 50))
    + list(range(2000, 20000, 100))
    + list(range(20000, 400000 + 1, 1000))
    )

# select a subset of checkpoints for Figure 1 (overview plot)
checkpoints = [0, 50, 100, 250, 500, 1_000, 2_500, 5_000, 10_000, 
               25_000, 50_000, 75_000, 100_000, 150_000, 200_000, 
               250_000, 300_000, 350_000, 400_000] 

# select a subset of checkpoints for Figure 2 (detailed plot)
checkpoints_detailed =  list(range(50_000, 410_000, 10_000))
# %%
# pythia models
# skip: you can't refactor the QK circuit when using rotary embeddings (as the QK matrix depends on the position of the query and key))
#pythia_160m = download_model("EleutherAI/pythia-160m")
#pythia_160m_v0 = download_model("EleutherAI/pythia-160m-v0")
#pythia_160m_deduped = download_model("EleutherAI/pythia-160m-deduped")
#pythia_160m_deduped_v0 = download_model("EleutherAI/pythia-160m-deduped-v0")
#pythia_160m_seed1 = download_model("EleutherAI/pythia-160m-seed1")
#pythia_160m_seed2 = download_model("EleutherAI/pythia-160m-seed2")
#pythia_160m_seed3 = download_model("EleutherAI/pythia-160m-seed3")

# %%
# test the original prompt to reproduce the results in the paper
original_prompt = "After John and Mary went to the store, John gave a bottle of milk to"
correct_answer = "Mary"
original_model = "gpt2-small"

# load the model and test the original prompt
model_ = HookedTransformer.from_pretrained(original_model,
            center_unembed=True,
            center_writing_weights=True,
            fold_ln=True,
            refactor_factored_attn_matrices=True)
utils.test_prompt(original_prompt, correct_answer, model_, prepend_bos=True, print_details=False)

# %%
# modify the prompt and sample the responses at different checkpoints
context_prefix = "John and Mary are friends. "
modified_prompt = context_prefix + original_prompt


# %%
context_prefix = "John and Mary are friends. "
prompt_prefix = "After they went to the store, John gave a bottle of milk to"
prompt = context_prefix + prompt_prefix
correct_answer = "Mary"



