
import utils as util
import numpy as np
import os

reconstructed_path = util.reconstructed_data_path
reconstructed_path ="D:/MSCRED/data/reconstructed/"
if not os.path.exists(reconstructed_path):
    print("no")
    
    os.makedirs(reconstructed_path)



reconstructed_path = reconstructed_path + "test_reconstructed.npy"
print(reconstructed_path)
# 예시 데이터 생성
result_example = np.random.rand(1, 30, 30, 3)  # shape를 맞춰야 함

# result_all 리스트에 예시 데이터 추가
result_all = [result_example]
result_all = np.asarray(result_all).reshape((-1, 30, 30, 3))
print(result_all.shape,reconstructed_path)
np.save(reconstructed_path, result_all)