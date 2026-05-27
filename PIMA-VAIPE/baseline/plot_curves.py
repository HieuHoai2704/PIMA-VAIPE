import re
import matplotlib.pyplot as plt

def plot_curves():
    log_file = 'train.log'
    losses = []
    accuracies = []
    
    with open(log_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    current_loss = None
    
    for line in lines:
        # Extract loss from the end of the epoch
        if "100%|" in line and "loss=" in line:
            # e.g., "loss=0.573]"
            match = re.search(r'loss=([0-9.]+)', line)
            if match:
                current_loss = float(match.group(1))
                
        # Extract validation accuracy
        if "Val accuracy:" in line:
            acc_match = re.search(r'Val accuracy:\s+([0-9.]+)', line)
            if acc_match:
                # Assuming accuracy is 0-1, convert to %
                acc = float(acc_match.group(1)) * 100
                if current_loss is not None:
                    losses.append(current_loss)
                    accuracies.append(acc)
                    current_loss = None
                    
    if not losses:
        print("No completed epochs found yet to plot.")
        return
        
    epochs = range(1, len(losses) + 1)
    
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(epochs, losses, 'b-', label='Train Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Training Loss')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(epochs, accuracies, color='orange', label='Test Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy (%)')
    plt.title('Test Accuracy')
    plt.legend()
    
    plt.tight_layout()
    
    output_file = 'learning_curves.png'
    plt.savefig(output_file)
    print(f"Successfully generated {output_file} from log with {len(losses)} epochs!")

if __name__ == '__main__':
    plot_curves()
