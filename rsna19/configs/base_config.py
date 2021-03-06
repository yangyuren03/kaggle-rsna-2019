class BaseConfig:
    nb_folds = 5

    train_dir = '/kolos/storage/ct/data/rsna/stage_1_train_images'
    test_dir = '/kolos/storage/ct/data/rsna/stage_1_test_images'
    test2_dir = '/kolos/storage/ct/data/rsna/stage_2_test_images'
    labels_path = "/kolos/storage/ct/data/rsna/stage_1_train.csv"
    # train_dir = '/mnt/data_fast/RSNA_Intracranial_Hemorrhage_Detection/stage_2_train_images'
    # test_dir = '/mnt/data_fast/RSNA_Intracranial_Hemorrhage_Detection/stage_2_test_images'
    # labels_path = "/mnt/data_fast/RSNA_Intracranial_Hemorrhage_Detection/stage_2_train.csv"

    data_root = "/kolos/m2/ct/data/rsna/"
    # data_root = "/mnt/data_fast_local/RSNA_Intracranial_Hemorrhage_Detection/"

    # Used for Dmytro's models
    checkpoints_dir = "/home/dmytro/ml/kaggle-rsna-2019/output/checkpoints"
    tensorboard_dir = "/home/dmytro/ml/kaggle-rsna-2019/output/tensorboard"
    oof_dir = "/home/dmytro/ml/kaggle-rsna-2019/output/oof"
    prediction_dir = "/home/dmytro/ml/kaggle-rsna-2019/output/prediction"

    # Used for Brainscan models
    model_outdir = '/kolos/m2/ct/models/classification/rsna/'
    # model_outdir = "/home/dmytro/ml/kaggle-rsna-2019/output/prediction"

    n_classes = 6
    csv_root_dir = None
