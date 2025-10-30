This file contains Python source code, a curated dataset (images & labels), requirements, and analysis for object detection model training.

# Evaluation (based on result)
**Precision-Recall curve**: Achieves strong average precision across classes, with best mAP@0.5 of 0.856  
**Loss Behavior**: Training and validation losses both peak then decrease—model is learning effectively, with minimal overfitting.  
**Confusion matrix**: Some classes perform better than others, indicating possible class imbalance.  
**Curve Analysis**:  
  - Precision/Recall and F1 curves show high performance at optimal confidence thresholds.  
  - Confusion matrices highlight main areas where the model confuses similar classes.  
**Label Distribution**: The dataset has a few under-represented classes. Enhancing these may further improve accuracy.  
- These results indicate a robust model for most classes, but further tuning and data balancing could help the weakest classes.  


