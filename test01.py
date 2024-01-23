import torch
bs = 8
label = 14
clabel = (torch.ones(bs) * label).type(torch.LongTensor)
print(clabel)

num_imgs_gaussian = 100
tmp = torch.multinomial(torch.tensor(clabel).float(), num_samples=num_imgs_gaussian, replacement=True)
print(tmp.shape)