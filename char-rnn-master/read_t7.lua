file = torch.DiskFile('sample.t7', 'r')
arrayNew = file:readObject()
print(arrayNew)