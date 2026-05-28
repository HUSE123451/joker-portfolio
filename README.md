# Joker Portfolio — 雨宫莲作品网站

## 使用方法

直接用浏览器打开 `index.html` 即可预览。

## 替换图片

网站中有 8 个占位图区域，准备好图片后替换即可：

### 需要的图片清单

| 位置 | 文件名建议 | 尺寸建议 | 说明 |
|------|-----------|----------|------|
| 首页 Hero | `hero-joker.png` | 500×667px | 雨宫莲全身立绘，建议透明背景PNG |
| 关于页面 | `about-joker.png` | 800×1000px | 角色特写/半身像 |
| 作品 01 | `work-01.png` | 800×800px | 战斗姿态 |
| 作品 02 | `work-02.png` | 800×800px | Persona 觉醒瞬间 |
| 作品 03 | `work-03.png` | 800×800px | 夜间行动场景 |
| 作品 04 | `work-04.png` | 800×800px | 总攻击演出 |
| 作品 05 | `work-05.png` | 800×800px | 日常形态 |
| 作品 06 | `work-06.png` | 800×800px | 终极技能特写 |

### 替换步骤

1. 将图片放入 `images/` 文件夹
2. 修改 HTML 中对应的占位 div，替换为 `<img>` 标签：

```html
<!-- 原始占位 -->
<div class="hero-image-placeholder">
  <div class="icon">🎭</div>
  <div class="label">Joker — 立绘位置</div>
</div>

<!-- 替换为 -->
<img src="images/hero-joker.png" alt="Joker" style="width:100%;height:100%;object-fit:cover;">
```

## 设计风格

- **极简色块碰撞** — Persona 5 标志性红黑白配色
- **对角线几何元素** — 来自 P5 的视觉语言
- **自定义光标** — 鼠标跟随 + 交互放大效果
- **滚动动画** — Intersection Observer 驱动的入场动画
- **数字计数器** — 统计数据动态展示
- **无限滚动字幕** — 底部装饰性文字跑马灯
- **响应式设计** — 适配桌面/平板/手机

## 图片来源建议

- **Pixiv** — 搜索 `雨宫莲 P5X`
- **Wallhaven** — 搜索 `persona 5 joker`
- **B站** — 搜索 `P5X 雨宫莲 壁纸素材包`
- **P5X 官方社媒** — 宣传图质量最高
