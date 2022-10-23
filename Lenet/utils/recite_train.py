# add path
import os, sys
project_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_path)
# add other's package
import torch
import torch.utils.data
import torch.nn
import torch.optim
# add my package
import utils.recite_dataloader
import utils.recite_model


train_loader = torch.utils.data.DataLoader(
    utils.recite_dataloader.LeNetDataSet(os.path.join(project_path, "data")).train_set,
    batch_size=36, shuffle=True, num_workers=0,
)
test_loader  = torch.utils.data.DataLoader(
    utils.recite_dataloader.LeNetDataSet(os.path.join(project_path, "data")).test_set,
    batch_size=10000, shuffle=False, num_workers=0,
)
test_data_iter = iter(test_loader)
test_image, test_label = test_data_iter.next()

# show img
def imshow(img):
    pass

net = utils.recite_model.LeNet()
loss_function = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(net.parameters(), lr = 0.001)

for epoch in range(1):  # loop
    running_loss = 0.0
    for step, data in enumerate(train_loader, start=0):
        inputs, labels = data   # [images, labels], data is a list
        # print(type(step), type(data), type(inputs))
        # print("step is {}, and inputs/images shape is {}, and labels shape is {}".format(step, inputs.shape, labels.shape))
        optimizer.zero_grad()
        outputs = net(inputs)
        # print("outputs shape is {}".format(outputs.shape))
        loss    = loss_function(outputs, labels)
        loss.backward()
        optimizer.step()    # update parameters in net

        # print(loss.shape)
        running_loss += loss.item()
        if step % 500 == 499:
            with torch.no_grad():   # 在下面的操作中不会自动计算梯度
                outputs = net(test_image)   # [batch, 10]
                # print("test_image's shape is {}, and outputs' shape is {}".format(test_image.shape, outputs.shape))
                predict_y = torch.max(outputs, dim=1)[1]
                print("predict_y's shape is {}".format(predict_y.shape))
                # print("sum is {}, item is {}".format((predict_y == test_label).sum(), (predict_y == test_label).sum().item()))
                accuracy = (predict_y == test_label).sum().item() / test_label.size(0) 

                print("[%d, %5d] train_loss: %.3f test_accuracy: %.3f" %(epoch + 1, step + 1, running_loss / 500, accuracy))
                running_loss = 0.0


save_path = os.path.join(project_path, "utils", "te")
torch.save(net.state_dict(), save_path)
