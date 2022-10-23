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
test_loader = torch.utils.data.DataLoader(
    utils.recite_dataloader.LeNetDataSet(os.path.join(project_path, "data")).test_set,
    batch_size=10000, shuffle=False, num_workers=0,
)
test_data_iter = iter(test_loader)
test_image, test_label = test_data_iter.next()

net = utils.recite_model.LeNet()
loss_function = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(net.parameters(), lr = 0.001)

for epoch in range(1):
    running_loss = 0.0
    for step, data in enumerate(train_loader, start=0):
        inputs, labels = data
        optimizer.zero_grad()
        outputs = net(inputs)
        loss = loss_function(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        if step % 500 == 499:
            with torch.no_grad():
                outputs = net(test_image)
                predict_y = torch.max(outputs, dim = 1)[1]
                accuracy = (predict_y == test_label).sum().item() / test_label.size(0)

                print("[{}, {:0>5d}] train_loss: {:.3f} test_accuracy: {:.3f}".format(epoch + 1, step + 1, running_loss / 500, accuracy))
                running_loss = 0.0


save_path = os.path.join(project_path, "utils", "te")
torch.save(net.state_dict(), save_path)