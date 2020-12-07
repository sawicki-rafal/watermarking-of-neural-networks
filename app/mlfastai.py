from fastai.vision.all import *

def get_architecture(arch_string):
    arch = {
        'resnet34': resnet34,
        'resnet50': resnet50
    }
    return arch.get(arch_string, resnet34)

# datablock = DataBlock(blocks=(ImageBlock, CategoryBlock),
#                       get_items=get_image_files,
#                       splitter=GrandparentSplitter(),
#                       get_y=parent_label,
#                       item_tfms=Resize(460),
#                       batch_tfms=aug_transforms(size=224, min_scale=0.75))
# dls = datablock.dataloaders(path)
# learn = cnn_learner(dls, get_architecture('resnet34'), metrics=error_rate)