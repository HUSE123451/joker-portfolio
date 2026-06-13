# JOKER Portfolio P5X 改进 — 工作记录

## 项目位置
`C:\Users\998\Desktop\joker-portfolio`

## 文件说明
- `index-original.html` — 原版备份（1312 行）
- `index.html` — 改进版（当前版本，1644 行）
- `images/` — 图片资源
- `audio/bgm.mp3` — 背景音乐

---

## 已完成的改进（6 个阶段）

### 阶段一：P5 加载动画 + 红色斜线切割
- Loading 动画从旋转环改为 P5 红色眼睛 SVG + 旋转菱形 + 进度条
- 每个 section 之间加入 45 度红色斜线条纹分割（`.section-slash`）
- CSS 类 `.section-slash` 和 `.section::before` 实现

### 阶段二：雷达图 + 预告信重做
- Skills 区域新增 SVG 六边形雷达图（STR/MAG/END/AGI/LUC/CHA）
- 数据点动态绘制 JS（`radarPoly` + `radarDot0-5`）
- 右侧配合六维属性条+数值显示
- Contact 预告信改为 P5 纸张风格（`.calling-card`）：米色背景、红色印章、横线纹理、签名

### 阶段三：Confidant 羁绊面板 + 日历
- 新增 Confidant section（`.confidant-grid`），8 个角色卡片含阿尔卡纳名和 10 级菱形等级
- 新增 P5 日历组件（`.p5-calendar`），展示关键剧情日期
- CSS: `.confidant-*` 和 `.p5-calendar-*` 系列

### 阶段四：音乐播放器 + 打字机效果
- 音乐播放器新增歌曲名显示（`.music-now`）和上一曲/下一曲按钮
- JS 中 `tracks` 数组支持多曲目切换（当前 3 首共用同一音频源）
- Story 区域 quote 文字添加逐字打字机效果（IntersectionObserver 触发）

### 阶段五：移动端 + 视觉效果
- 移动端导航从六边形改为 P5 红色倾斜按钮 `skewX(-12deg)`
- Gallery hover 红色 flash 闪光效果（`@keyframes flashRed`）
- Story 时间线改为 Mementos 晶体风格（六边形节点 + 发光 + 模糊光晕）
- 响应式适配新增区域（768px/480px）

### 阶段六：音乐 + 移动端 + 视觉细节
- 音乐曲目更名：bgm.mp3 → Full Moon, Full Life，新增 full_moon_full_life.mp3（Instrumental）和 tofubeats_remix.mp3（星と僕らと tofubeats Remix）
- 音乐文件已下载完成：通过网易云音乐 API 获取（Full Moon, Full Life: 4.5MB, 星と僕らと: 3.5MB）
- 移动端新增 Confidant 羁绊面板 slide（slide 6）和 P5X 关键日期日历 slide（slide 7）
- Story 区域新增 Mementos 红色水晶背景纹理（`.mementos-bg`），含浮动晶体粒子动画
- Hero 区域新增 P5X 风格化 Logo（斜体 + 红色斜线 + PERSONA 5X 副标题），桌面端和移动端均已添加
- Confidant 数据修正：祐介 太阳→月亮（The Moon），佐仓惣治郎 塔→法皇（The Hierophant），符合 P5 原作设定

---

## 待完成 / 可改进

1. **P5X Logo 字体**：可寻找更还原的 P5X 官方风格化字体替换当前 CSS 模拟效果
2. **移动端 Confidant 卡片**：可在卡片中增加 `confidant-desc` 简短描述，与桌面端保持一致

---

## 技术要点

- 纯 HTML/CSS/JS，无依赖
- 图片通过 jsDelivr CDN 加载：`https://cdn.jsdelivr.net/gh/HUSE123451/joker-portfolio@main/`
- 移动端使用自定义 slide 视口系统（`.m-viewport`），与桌面端独立
- 动画使用 IntersectionObserver 触发，支持滚动揭示
