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

## 阶段七：视觉增强 + 交互打磨

### 字体升级
- P5X Logo 字体从 Bebas Neue 改为 **Anton**（Google Fonts），更接近 P5X 官方粗体压缩风格
- 新增 **Russo One** 字体用于副标题 PERSONA 5X
- 导航栏 Logo 同步使用 Anton 字体 + 斜体效果
- Logo 文字增加外发光 `text-shadow` + `text-stroke` 效果

### Hero 粒子特效
- 新增 Canvas 粒子系统（`#heroParticles`），60 个浮动红色/白色光点
- 粒子带脉冲呼吸效果，颜色随机（红/亮红/白）
- 每个粒子带 3 倍大小的光晕层，营造暗夜氛围

### 交互动效增强
- **Hero 视差滚动**：背景图片随滚动以 0.3 倍速移动
- **统计数字计数动画**：LEVEL/ARCANA 数字从 0 滚动到目标值
- **技能卡片鼠标跟随光效**：hover 时 radial-gradient 跟随鼠标位置
- **卡片悬浮增强**：skill-card/confidant-card hover 加大位移 + 发光阴影
- **图鉴边框效果**：gallery-item hover 时红色边框 + 更流畅的 overlay 动画
- **预告信卡片**：hover 微微倾斜 + 印章放大旋转 + 更强阴影
- **怪盗档案图片**：hover 亮度提升 + 红色边框呼吸动画
- **对话框**：hover 红色发光边框
- **斜线分割**：红色斜线 + 水平线带呼吸脉冲动画
- **Hero 标题红色文字**：呼吸发光 `text-shadow` 动画

### 移动端打磨
- 新增 **SWIPE 提示**：首次进入显示滑动箭头提示，滑动后自动隐藏
- **卡片点击反馈**：confidant/skill/calendar 卡片 `:active` 缩放 + 发光
- **Slide 进入动画**：stat 数字在 about slide 进入时触发计数动画

---

## 阶段八：P5X 暂停背景 — 星星铺满背景

### 背景来源
- 从 `https://p5x.jp/` 爬取官网 HTML → 找到 CSS 引用 `bg.webp`
- 下载 `bg.webp`（2340x760, 440KB）分析像素颜色和星星布局
- 官网星星特征：深灰色同心五角星轮廓，完全铺满背景，无黑色空隙

### P5X 官网背景精确参数（从 bg.webp 分析）
- 背景色：`#060403`（近乎纯黑）
- 星星最亮色：`rgb(38,38,38)`（极暗灰）
- 星星最暗色：`rgb(7,5,6)`
- 同心层数：5-6 层
- 内层比例：~0.35
- 线条粗细：~4px
- 层间收缩：~18%
- 布局：网格均匀分布 + 随机抖动，星星适度重叠

### 实现过程（多次迭代）

**迭代 1**：基础 Canvas 星星
- 10 顶点五角星（5外+5内），同心层绘制
- 网格 180px，4 层，lineWidth 2

**迭代 2**：用户反馈"太少了星星"
- 增加到 ~2150 颗星，4 密度层

**迭代 3**：用户反馈"恐怖游戏观感，太乱，很多空"
- 改为网格排列，70-80% 大星，网格 180px

**迭代 4**：用户反馈"空白太多，星星要线段不要线条，太细"
- 网格 140px，lineWidth 2.5，线段间隙 `lr*0.08`

**迭代 5**：爬取 P5X 官网分析真实参数
- 下载 `bg.webp`，像素分析颜色值
- 发现 P5X 是网格均匀铺满 + 适度重叠

**迭代 6**：用户反馈"完全随机你个蛋，人家是铺满的"
- 改为网格 130px + 随机抖动

**迭代 7**：用户反馈"还是没铺满"
- 网格 90px，8 层，lineWidth 3.5

**迭代 8（当前版本）**：极端加密
- 基底层：65px 网格，80-110px 半径，10 层同心
- 大星：75px 网格，55-85px 半径，8 层
- 中星：85px 网格，35-60px 半径，7 层
- 小星：95px 网格，18-35px 半径，5 层
- 层间收缩 13%，lineWidth 4，间隙 `lr*0.03`

### 当前状态
- 代码已保存到 `index.html`
- **未验证最终效果** — 需要用户手动刷新页面暂停音乐查看
- 如果仍不满意，可能需要：进一步缩小网格间距、增加层数、或改用直接加载 `bg.webp` 图片作为背景

---

## 待完成 / 可改进

1. **P5X Logo 字体**：已升级为 Anton，可进一步寻找 P5X 官方 TTF 字体替换
2. **移动端 Confidant 卡片**：已完成 confidant-desc 添加
3. **P5X 暂停背景**：当前 Canvas 星星可能仍需调整，备选方案：直接使用下载的 `bg.webp` 作为 tiled 背景图片（最简单最还原）

---

## 技术要点

- 纯 HTML/CSS/JS，无依赖
- 图片通过 jsDelivr CDN 加载：`https://cdn.jsdelivr.net/gh/HUSE123451/joker-portfolio@main/`
- 移动端使用自定义 slide 视口系统（`.m-viewport`），与桌面端独立
- 动画使用 IntersectionObserver 触发，支持滚动揭示
