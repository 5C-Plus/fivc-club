# 用户密码管理API使用指南

## 概述

本文档介绍Django项目中用户密码管理功能的API使用方法，包括用户修改密码和管理员设置用户密码两个功能。

## API端点

### 1. 用户信息更新

**端点**: `PATCH /api/users/self/`

**描述**: 允许已认证用户更新自己的基本信息

**请求头**:
```
Authorization: Bearer <session_key>
Content-Type: application/json
```

**请求体**:
```json
{
    "email": "newemail@example.com",
    "first_name": "新的名字",
    "last_name": "新的姓氏"
}
```

**成功响应** (200 OK):
```json
{
    "username": "testuser",
    "email": "newemail@example.com",
    "first_name": "新的名字",
    "last_name": "新的姓氏",
    "is_staff": false,
    "is_active": true,
    "date_joined": "2023-01-01T00:00:00Z"
}
```

**错误响应**:
- 401 Unauthorized: 用户未认证
- 400 Bad Request: 验证失败（邮箱已被使用等）

### 2. 用户修改密码

**端点**: `POST /api/users/change-password/`

**描述**: 允许已认证用户修改自己的密码

**请求头**:
```
Authorization: Bearer <session_key>
Content-Type: application/json
```

**请求体**:
```json
{
    "old_password": "当前密码",
    "new_password": "新密码",
    "confirm_password": "确认新密码"
}
```

**成功响应** (200 OK):
```json
{
    "message": "密码修改成功"
}
```

**错误响应**:
- 401 Unauthorized: 用户未认证
- 400 Bad Request: 验证失败（旧密码错误、新密码不符合要求等）

### 3. 管理员设置用户密码

**端点**: `POST /api/users/<username>/set-password/`

**描述**: 允许管理员为指定用户设置新密码

**请求头**:
```
Authorization: Bearer <admin_session_key>
Content-Type: application/json
```

**请求体**:
```json
{
    "new_password": "新密码",
    "confirm_password": "确认新密码"
}
```

**成功响应** (200 OK):
```json
{
    "message": "用户 <username> 的密码设置成功"
}
```

**错误响应**:
- 401 Unauthorized: 用户未认证
- 403 Forbidden: 非管理员用户
- 404 Not Found: 用户不存在
- 400 Bad Request: 验证失败

## 密码验证规则

系统使用Django内置的密码验证器，包括：

1. **UserAttributeSimilarityValidator**: 密码不能与用户信息过于相似
2. **MinimumLengthValidator**: 密码最少8个字符
3. **CommonPasswordValidator**: 密码不能是常见密码
4. **NumericPasswordValidator**: 密码不能全是数字

## 使用示例

### JavaScript/Fetch示例

#### 用户更新信息
```javascript
const updateUserInfo = async (email, firstName, lastName) => {
    const response = await fetch('/api/users/self/', {
        method: 'PATCH',
        headers: {
            'Authorization': `Bearer ${sessionKey}`,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: email,
            first_name: firstName,
            last_name: lastName
        })
    });

    if (response.ok) {
        const result = await response.json();
        console.log('用户信息更新成功:', result);
        return result;
    } else {
        const error = await response.json();
        console.error('用户信息更新失败:', error);
        throw error;
    }
};
```

#### 用户修改密码
```javascript
const changePassword = async (oldPassword, newPassword, confirmPassword) => {
    const response = await fetch('/api/users/change-password/', {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${sessionKey}`,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            old_password: oldPassword,
            new_password: newPassword,
            confirm_password: confirmPassword
        })
    });
    
    if (response.ok) {
        const result = await response.json();
        console.log(result.message);
    } else {
        const error = await response.json();
        console.error('密码修改失败:', error);
    }
};
```

#### 管理员设置用户密码
```javascript
const setUserPassword = async (username, newPassword, confirmPassword) => {
    const response = await fetch(`/api/users/${username}/set-password/`, {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${adminSessionKey}`,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            new_password: newPassword,
            confirm_password: confirmPassword
        })
    });
    
    if (response.ok) {
        const result = await response.json();
        console.log(result.message);
    } else {
        const error = await response.json();
        console.error('密码设置失败:', error);
    }
};
```

### Python/Requests示例

#### 用户修改密码
```python
import requests

def change_password(session_key, old_password, new_password, confirm_password):
    url = 'http://localhost:8000/api/users/change-password/'
    headers = {
        'Authorization': f'Bearer {session_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'old_password': old_password,
        'new_password': new_password,
        'confirm_password': confirm_password
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print(response.json()['message'])
    else:
        print('密码修改失败:', response.json())
```

## 安全注意事项

1. **认证要求**: 所有密码相关操作都需要用户认证
2. **权限控制**: 只有管理员可以设置其他用户的密码
3. **密码强度**: 系统会验证新密码的强度
4. **会话管理**: 修改密码后建议重新登录以获取新的会话
5. **日志记录**: 密码修改操作会被记录（不包含密码内容）

## 错误处理

常见错误及处理方法：

- **当前密码不正确**: 提示用户重新输入当前密码
- **新密码和确认密码不一致**: 提示用户检查密码输入
- **新密码不能与当前密码相同**: 提示用户选择不同的新密码
- **密码强度不够**: 根据验证器提示改进密码强度
- **用户不存在**: 检查用户名是否正确
- **权限不足**: 确认用户是否有相应权限

## 测试

项目包含完整的测试用例，位于 `modules/users/tests_password.py`，可以运行以下命令进行测试：

```bash
python manage.py test modules.users.tests_password
```
