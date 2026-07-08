"""
API 接口自动化测试示例
目标：Swagger Petstore (https://petstore.swagger.io/)
这是一个标准的 RESTful API，适合练习接口测试

运行方式：
    cd api-tests/
    pip install -r requirements.txt
    pytest test_bookstore_api.py -v
"""

import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2"


class TestPetAPI:
    """Pet 模块接口测试"""

    @pytest.fixture
    def pet_data(self):
        """测试数据：创建一个宠物"""
        return {
            "id": 0,  # 0 表示自动生成 ID
            "name": "doggie",
            "photoUrls": ["https://example.com/photo.jpg"],
            "status": "available"
        }

    def test_add_pet(self, pet_data):
        """添加宠物 - 正常流程"""
        resp = requests.post(f"{BASE_URL}/pet", json=pet_data)
        assert resp.status_code == 200
        pet_id = resp.json()["id"]
        assert resp.json()["name"] == "doggie"
        assert resp.json()["status"] == "available"
        # 保存 ID 供后续测试使用（实际项目会放到类变量或 fixture 中）
        return pet_id

    def test_get_pet_by_id(self, pet_data):
        """按 ID 查询宠物 - 正常流程"""
        # 先添加一个宠物
        add_resp = requests.post(f"{BASE_URL}/pet", json=pet_data)
        pet_id = add_resp.json()["id"]

        # 按 ID 查询
        resp = requests.get(f"{BASE_URL}/pet/{pet_id}")
        assert resp.status_code == 200
        assert resp.json()["name"] == "doggie"

    def test_get_pet_not_found(self):
        """按 ID 查询不存在的宠物 - 异常流程"""
        resp = requests.get(f"{BASE_URL}/pet/999999999")
        assert resp.status_code == 404

    def test_find_pets_by_status(self):
        """按状态查找宠物"""
        resp = requests.get(
            f"{BASE_URL}/pet/findByStatus",
            params={"status": "available"}
        )
        assert resp.status_code == 200
        pets = resp.json()
        assert len(pets) > 0
        for pet in pets:
            assert pet["status"] == "available"

    def test_update_pet(self, pet_data):
        """更新宠物信息"""
        add_resp = requests.post(f"{BASE_URL}/pet", json=pet_data)
        pet_id = add_resp.json()["id"]

        # 更新
        pet_data["id"] = pet_id
        pet_data["name"] = "doggie_updated"
        pet_data["status"] = "sold"

        resp = requests.put(f"{BASE_URL}/pet", json=pet_data)
        assert resp.status_code == 200
        assert resp.json()["name"] == "doggie_updated"
        assert resp.json()["status"] == "sold"

    def test_delete_pet(self, pet_data):
        """删除宠物"""
        add_resp = requests.post(f"{BASE_URL}/pet", json=pet_data)
        pet_id = add_resp.json()["id"]

        # 删除
        resp = requests.delete(f"{BASE_URL}/pet/{pet_id}")
        assert resp.status_code == 200

        # 验证已删除
        get_resp = requests.get(f"{BASE_URL}/pet/{pet_id}")
        assert get_resp.status_code == 404

    def test_add_pet_invalid_data(self):
        """添加宠物 - 异常场景：空数据"""
        resp = requests.post(f"{BASE_URL}/pet", json={})
        # 期望返回 4xx 错误
        assert resp.status_code >= 400


class TestStoreAPI:
    """商店模块接口测试"""

    def test_get_inventory(self):
        """获取仓库库存"""
        resp = requests.get(f"{BASE_URL}/store/inventory")
        assert resp.status_code == 200
        inventory = resp.json()
        # 验证返回的是键值对
        assert isinstance(inventory, dict)
        print(f"\n当前库存: {inventory}")

    def test_place_order(self):
        """下订单"""
        order = {
            "id": 0,
            "petId": 1,
            "quantity": 2,
            "shipDate": "2026-07-08T10:00:00.000Z",
            "status": "placed",
            "complete": True
        }
        resp = requests.post(f"{BASE_URL}/store/order", json=order)
        assert resp.status_code == 200
        order_id = resp.json()["id"]
        assert resp.json()["status"] == "placed"

        # 验证订单存在
        get_resp = requests.get(f"{BASE_URL}/store/order/{order_id}")
        assert get_resp.status_code == 200


if __name__ == "__main__":
    # 直接运行测试
    pytest.main([__file__, "-v"])
