# SWOT 发展现状与研究方向综合报告

> 基于 `C:\Users\咀嚼\Desktop\SWOT` 文件夹内 19 份学术论文与会议材料，以及已有《文献阅读梳理.md》形成。资料覆盖 2023—2026 年，重点反映 SWOT 在轨运行后从性能验证走向科学发现和业务应用的最新进展。

## 摘要

地表水与海洋地形（Surface Water and Ocean Topography, SWOT）任务的核心突破，是以 Ka 波段雷达干涉仪（KaRIn）将传统沿轨一维测高扩展为宽刈幅二维高程成像。现有文献表明，SWOT 已经完成了从“仪器能力证明”到“可开展新科学研究”的关键转折：在海洋领域，全球亚中尺度涡、内孤立波和细尺度海表结构首次得到二维观测[19]；在内陆水文领域，湖泊水位、河宽、水面坡降、流量和河道蓄水变化开始形成近全球产品[16–18]；在海岸带和固体地球领域，潮间带地形、海洋重力异常与海底地形反演成为重要的拓展方向[12–14]。

但 SWOT 的高空间分辨率也暴露出新的限制。仪器噪声在部分场景下已不再是主要误差，湿对流层小尺度变化、内潮混叠、近岸辐射计陆地污染、复杂河网先验几何、时间采样不足以及跨任务基准不一致，正在成为制约物理解释和业务化应用的关键因素[1,7,10–11]。因此，下一阶段研究重点不应只是继续展示“看得更细”，而应转向“信号可分离、误差可追溯、结果可验证、产品可融合、过程可解释”。

本报告提出一个六层分析框架：观测能力、产品与质量控制、误差校正、信息融合、过程反演、验证与应用；并建议优先布局动态误差场重建、内潮—涡旋信号分离、多源时空融合、复杂水体对象化处理、物理约束人工智能及可复现基准体系。

## 1. 文献范围与分析方法

本次阅读对象包括 18 篇期刊论文和 1 份 KaRIn 拓展应用会议材料。主题分布如下：

| 主题 | 数量 | 代表问题 |
|---|---:|---|
| 海洋细尺度动力、内波与多源融合 | 6 | 亚中尺度涡、内孤立波、内潮校正、L3 融合 |
| 内陆水文与河流湖泊 | 6 | 水位、流量、辫状河、季节性湖泊、河道蓄水 |
| 海岸带与潮间带 | 2 | 超强潮河口、潮间带数字高程模型 |
| 海洋重力与海底地形 | 2 | 高频重力异常、深度神经网络测深 |
| 误差校正与定标验证 | 2 | KaRIn 几何性能、湿对流层残差 |
| KaRIn 拓展应用 | 1 | DInSAR、高度改正、后向散射和相干性 |

分析不以应用场景简单罗列为终点，而是沿着完整的信息链梳理：

```text
KaRIn二维观测
    ↓
L1/L2产品与质量标志
    ↓
几何、轨道、大气、潮汐和地球物理校正
    ↓
SWOT—传统测高—光学—SAR—模型—现场观测融合
    ↓
水位/坡降/流量/涡旋/内波/重力/地形等过程量反演
    ↓
独立验证、不确定度传播与科学/业务应用
```

该框架的价值在于：任何应用效果不佳，都可以沿链条定位是观测条件、产品处理、校正模型、先验数据、反演方法还是验证设计的问题。

## 2. SWOT 的技术能力与阶段判断

### 2.1 核心能力已经得到在轨验证

SWOT 最明确的优势是二维宽刈幅和高空间分辨率。Bass Strait 的九个 GNSS 浮标验证显示，标准 2 km 像元产品的 KaRIn 海面高噪声上限约为 7.0 mm，250 m 未平滑产品约为 13.0 mm；KaRIn 绝对高度偏差约 10.3 mm，显著波高 RMSE 为 0.22 m[7]。这说明在开阔、近岸陆架等复杂环境中，KaRIn 本体性能已达到高水平。

与此同时，“分辨率提高”不是简单地把传统测高产品做得更密。SWOT 直接改变了可观测对象：传统测高适合沿轨统计和大尺度海洋环流，SWOT 则能观察涡旋边界、锋面、条带状内波、分汊河道间的水面差异和潮间带细部高程[2,6,10,12,19]。换言之，研究对象已经从一维剖面上的点和线，转向二维场中的形态、连通性和梯度。

### 2.2 任务正处于“科学发现期向融合应用期过渡”的阶段

现有成果可分为三个阶段：

1. **性能证明**：利用 GNSS 浮标、水位站、ICESat-2、船测重力和传统测高验证 KaRIn 精度与误差特征[7,12–13,16]。
2. **新现象发现**：全球亚中尺度动力、内孤立波、辫状河多通道水面动力和潮间带地形等过去难以观测的对象开始被解析[10,12,19]。
3. **产品融合与业务化**：SWOT 与 DUACS、Sentinel-1/2/3、OPERA、水文站网、HYCOM 及深度学习结合，形成可连续使用的 L3 产品、专题数据集和反演模型[1,4,6,9,12,14]。

当前第三阶段刚刚起步。真正的业务化仍受 21 天科学轨道重访周期、质量标志筛选造成的有效观测损失、不同传感器时空尺度不一致及高频误差残差限制[5,8,11,18]。

## 3. 主要研究领域的发展现状

### 3.1 海洋亚中尺度动力：从区域个例走向全球观测

Archer 等基于 SWOT 展示了全球 1—100 km 亚中尺度涡和非线性内波，指出这些过程对海洋能量、垂向热量与碳输运、生态系统及气候系统的影响可能高于过去估计[19]。这一工作确立了 SWOT 的核心海洋科学价值：亚中尺度过程不再只能依赖局地现场观测或高分辨率模式推断。

在热带西太平洋，SWOT 每个约 10.5 天子周期识别到 273 个亚中尺度涡，而 DUACS 仅识别到 13 个；对中尺度涡，两者数量接近[15]。这一对比说明 SWOT 的增量价值主要集中在较小尺度，而不是替代传统多星测高对中大尺度、连续时间序列的优势。

南海研究进一步表明，SWOT 可作为高分辨率“真实性参照”，评价 AVISO 和二维变分融合图中的涡旋边界。相较 AVISO，2DVAR 与 SWOT 在小尺度结构上更一致[2]，说明 SWOT 不仅是新观测源，也可以成为训练、调参与验证传统多星融合算法的基准。

### 3.2 内波与内潮：观测能力提升，同时成为信号分离难题

SWOT 的二维海表高度异常能够呈现内孤立波条带结构。基于深度学习的 SWOT_IWD 框架处理了 2023—2025 年全球 13 个内波高发区的 21,682 个过境轨次，识别 2,011 个含内波信号的轨次和 3,264 个内波信号，数据集平均精度为 91.21%[6]。这标志着内波研究正从少量个例判读转向全球专题数据集和自动检测。

但内潮，尤其非相干内潮，会与亚中尺度海表高度信号发生混叠。2026 年的全球内潮建模研究表明，将数据同化海洋预报模型用于显式刻画演变中的中尺度背景，可以预测过去被视为混沌的非相干内潮；对总内潮信号进行校正后，相比现有经验方法误差降低 59%[1]。这提示后续研究应从静态经验改正转向状态依赖、时变的动力校正。

### 3.3 海洋多星融合：SWOT 与传统测高是互补而非替代关系

DUACS L3 扩展研究将 SWOT 二维刈幅数据纳入已有多星测高体系，处理异常像元、跨任务定标和一维/二维观测合并。其科学意义在于把 SWOT 的高空间分辨率嵌入近 30 年的稳定多星时间序列[4]。

当前最佳策略是尺度分工：传统星座提供长时间、稳定、较高时间分辨率的背景场；SWOT 提供精细二维结构和局地梯度[2,4,15]。下一步的难点是避免融合过程中过度平滑 SWOT 的高波数信号，同时抑制条带误差、内潮和小尺度大气残差[1,7,11]。

### 3.4 内陆水文：从水位产品走向流量与蓄水变化

全球水位验证结果显示，SWOT 湖泊产品相对 Hydroweb 和 G-REALM 的平均绝对误差分别小于 0.5 m 和 0.3 m；河流水位全球平均误差小于 0.15 m[16]。希腊湖泊研究在严格筛除相位噪声较大的像元后，湖泊平均水位相对永久水位站达到约 13—19 cm 精度，但也指出有效时间覆盖低于预期，像元级高分辨率常因测量离散度过大而难以直接利用[5]。

流量反演框架利用水面高程、河宽、坡降和先验河流参数估计河流流量。文献预计，全球约三分之二河段的流量不确定度可低于 30%，几乎所有河段的时间变化误差可控制在 15% 左右；主要瓶颈是先验参数引入的系统偏差，而不是单次观测的随机误差[17]。

2026 年全球河道研究进一步利用 SWOT 首个完整水文年，对 126,674 个河段估计河道几何和月尺度蓄水变化，得到全球河流年内蓄水变化范围 313.1 ± 129.5 km³。该值低于既有模型估计，也暴露出北极冻结河流、极端干旱年份和有限重访造成的漏采样问题[18]。

### 3.5 复杂河流与极端事件：对象化处理的重要性上升

标准 RiverSP 依赖简化中心线，难以表达辫状河的多通道结构。融合 Sentinel-2 水体掩膜与 SWOT PIXC 后，雅鲁藏布江—布拉马普特拉河平行河道间可出现约 0.5 m 水面高程差和 2 cm/km 坡降差[10]。这说明复杂河网必须从“单中心线”转向“动态河道对象 + 多通道拓扑”。

Death Valley 的季节性 Lake Manly 案例则展示了 SWOT 水位与 OPERA 水体范围产品协同监测极端降水后临时湖泊形成和消退的能力[9]。此类事件监测将 SWOT 从静态水资源清查推向灾害响应和气候适应应用，但需要与高频光学、SAR 和降水数据共同使用。

### 3.6 海岸带与潮间带：高价值、高复杂度的试验场

在 Bristol Channel—Severn Estuary 超强潮环境中，经过水位相关尺度偏差校正后，SWOT L3 水位相对单站潮位计的 RMSD 为 0.059—0.150 m，所有站点合并 RMSD 为 0.137 m。二维水位图能够呈现河流入海、沙洲移动和风暴潮等沿海连续体过程，但科学轨道 21 天重访不足以稳定捕获高频过程[8]。

江苏潮间带研究以 Sentinel-2 确定潮间带范围，利用 DBSCAN 清理 SWOT L2_HR_PIXC 点云，并与虚拟潮位计信息结合生成 10 m DEM。相对 ICESat-2，多周期和单周期 RMSE 分别为 0.24 m 和 0.41 m[12]。这证明无需地面实测也可开展大范围潮间带制图，但方法依赖低潮过境，且需要更好的水陆分类和跨周期基准统一。

### 3.7 海洋重力与海底地形：从测高副产品走向地球物理应用

SWOT 的密集二维海面高数据可增强高频海洋重力异常。与 CryoSat-2 相比，SWOT 在 2—4 km 点距上的高频重力恢复精度提高约 6.8%—7.9%，显示其对短波重力信号最具优势[13]。

在西北太平洋，SWOT 重力数据与单波束船测水深结合深度神经网络，海底地形预测 RMS 约 97.5 m，较重力—地质法和 Smith–Sandwell 方法分别提高 19.5% 和 9.9%[14]。这类方法有望填补船测空白，但结果高度依赖训练样本的空间代表性，跨海域泛化和物理一致性仍需验证。

### 3.8 拓展应用：KaRIn 数据价值尚未完全释放

会议材料表明，基于 KaRIn SLC 单程差分干涉相位可估算相对参考 DEM 的高度改正；多时相后向散射可用于农田、森林、城市、水体区分，并具有作物、土壤湿度和土地利用研究潜力。水面高后向散射区的单程相干性通常较高，而陆地相干性常受接近噪声底的信号限制[3]。

该方向目前多为探索性案例[3]。真正形成稳定应用，需要从 L1B SLC 出发建立辐射定标、几何定位、入射角归一化、时序一致性及独立地面验证流程。

## 4. 关键限制与误差机制

### 4.1 小尺度大气改正已成为高波数解释的瓶颈

澳大利亚沿岸研究表明，15—80 km 尺度上的湿对流层路径延迟可达到 SWOT 误差预算的两倍；距海岸约 50 km 内，辐射计还存在厘米级陆地污染偏差[11]。这类残差与真实亚中尺度海表信号处于相近尺度和量级，若不处理，可能把大气结构误判为海洋动力结构。

### 4.2 地球物理改正误差可超过仪器噪声

Bass Strait 验证显示，浮标间距增大后 SSH 差异误差上升，部分原因来自地球物理改正[7]。滚转/相位误差、基线伸缩、定时与相位偏差可表现为跨轨线性、二次或左右刈幅独立偏移[7]。仪器本身足够精密后，误差研究必须从单一“噪声水平”转向空间结构和误差协方差。

### 4.3 时间采样限制高频过程与极值估计

SWOT 的 21 天科学轨道适合全球覆盖，但无法单独重建潮汐、风暴潮、洪峰、快速沙洲迁移和短生命周期涡旋[8,18]。校准验证期的日尺度观测极具价值，但时间较短[8]。多星融合、动力模型同化和事件触发式联合观测是弥补时间采样不足的必要路径[1,4]。

### 4.4 复杂边界和先验几何会引入对象定义误差

辫状河、三角洲、潮间带、湖岸和近岸岛礁都存在快速变化的水陆边界[8,10,12]。若继续依赖静态河网、固定中心线或粗分辨率水体掩膜，误差会在后续的宽度、坡降、流量和蓄水反演中被放大[10,17–18]。

### 4.5 高分辨率并不自动等于高可用性

PIXC 等高分辨率产品包含丰富信息，也伴随相位噪声、离群点和分类错误[5,10,12]。湖泊研究已经显示，在像元级尺度上，数据离散度可能掩盖预期优势[5]。必须把质量标志、相位噪声、邻域一致性和水体对象约束纳入统一质量控制。

## 5. SWOT 战略矩阵

这里的 SWOT 矩阵用于概括该卫星任务的发展态势，与卫星名称形成同名但不同义的分析。

| 维度 | 主要判断 |
|---|---|
| **优势 Strengths** | 二维宽刈幅；毫米至厘米级海面测高能力；能解析 1—100 km 海洋过程；同步测量河流水位、宽度和坡降；全球一致观测；L1B—L3 多层产品体系[7,17,19]。 |
| **劣势 Weaknesses** | 21 天重访限制高频过程；近岸湿对流层和辐射计污染；复杂水陆边界分类困难；条带与几何误差具有空间相关性；高分辨率产品处理门槛高[5,7–8,10–11]。 |
| **机会 Opportunities** | 与多星测高、Sentinel、ICESat-2、OPERA、现场站网及动力模型融合；全球内波/涡旋/河道蓄水数据集；海洋重力和海底地形；物理约束人工智能；灾害与水资源业务服务[1,4,6,9,12–14,18]。 |
| **威胁 Threats** | 把残余改正误差误判为新物理信号；不同版本产品造成结论不可比；AI 对区域样本过拟合；缺少全球独立验证；数据量和计算门槛阻碍复现[7,11,14]。 |

由此形成四类策略：

- **SO 策略**：利用二维高分辨率优势建设全球专题数据集，并通过多源融合扩展时间维度。
- **WO 策略**：用模型同化和跨传感器校正弥补时间采样及误差场不足。
- **ST 策略**：依托全球一致观测建立标准化基准，防止局地案例和算法过拟合。
- **WT 策略**：明确产品版本、质量标志和不确定度传播，避免把处理伪影解释为科学发现。

## 6. 建议的重点研究方向

### 方向一：面向高波数海洋信号的动态误差场重建

联合高分辨率数值天气模式、GNSS 水汽、辐射计和 SWOT 交叉点数据，构建 10—100 km 尺度湿对流层残差场；同时估计滚转、基线、定时和左右刈幅偏差。目标不是得到单一校正值，而是输出随时间和空间变化的误差场及协方差。该方向直接回应近岸湿对流层残差和空间相关几何误差问题[7,11]。

### 方向二：内潮—内波—涡旋的可解释信号分离

将数据同化海洋模式、潮汐谐波、时空谱分析和深度学习结合，区分相干内潮、非相干内潮、内孤立波及平衡流。建议以“物理守恒 + 数据驱动残差”架构替代纯图像分类，并在独立过境和不同海区开展泛化验证[1,6,19]。

### 方向三：保留高波数信息的多星测高融合

在 DUACS 类框架中显式建模 SWOT 的二维采样和空间相关误差，研究多尺度或谱域融合，避免客观分析将细尺度信号过度平滑。产品应同时给出背景场、SWOT 增量场和尺度依赖不确定度[2,4,15]。

### 方向四：复杂河网的动态拓扑与对象化水文反演

利用 Sentinel-1/2 或高分辨率水体掩膜动态更新河道中心线和分汊拓扑，将 PIXC 像元聚合到真实河道对象，而非固定先验河段。进一步估计各支汊流量分配、坡降变化、泥沙输运潜势及洪水期连通性[10,17–18]。

### 方向五：湖泊与河流有效观测率提升

围绕相位噪声标准差、质量标志、邻域一致性和多周期稳定性建立分层筛选规则；区分“精度”和“有效覆盖率”两个指标。对小湖泊、窄河流和冰冻水体，应建立专门的场景化质量模型[5,16,18]。

### 方向六：海岸带陆—海连续体的多源高频重建

将 SWOT 的二维空间快照与潮位计、SAR、光学、波浪模式和水动力模型结合，重建河口水位梯度、风暴潮、沙洲迁移和潮间带地形变化。研究重点应从单次精度验证转向事件尺度的质量控制和过程闭合[8–9,12]。

### 方向七：海洋重力与海底地形的物理约束人工智能

在 DNN 中引入重力—地形传递关系、水深分区和构造先验，开展留一海区、留一构造类型和不同船测密度条件下的泛化实验。成果应报告空间分辨率、RMS、系统偏差及不确定度，而不只报告整体精度提升百分比[13–14]。

### 方向八：KaRIn SLC 拓展应用与 L1 级处理链

系统评估单程 DInSAR 高度改正、后向散射时序和相干性在洪泛区、农田、湿地、冻融及城市变化中的可用性。优先建立可复现的 SLC 聚焦、干涉、解缠、地理编码和辐射定标基准数据集[3]。

### 方向九：版本化、可复现的全球验证基准

建立覆盖开阔海、近岸、河口、湖泊、辫状河、冰冻河流和潮间带的验证样区；统一记录产品版本、改正项、质量筛选和参考基准。对每个专题产品同时给出精度、完整率、有效观测率和区域可迁移性[5,7–8,10–12,16,18]。

## 7. 可执行的研究技术路线

建议采用“一个底座、两类校正、三种融合、四级验证”的路线：

1. **一个数据底座**：统一管理 SWOT L1B SLC、L2 PIXC/SSH、L3、多星测高、Sentinel、ICESat-2、站点和模式数据，保留产品版本及处理日志[3–4,6,12]。
2. **两类校正**：一类是几何与仪器误差，另一类是湿对流层、潮汐、内潮等地球物理误差；均输出不确定度[1,7,11]。
3. **三种融合**：观测—观测融合、观测—模型同化、物理—机器学习融合[1,4,6,14]。
4. **四级验证**：像元级、对象级、过程级、跨区域泛化验证[5,7–8,10,12,16]。

优先级建议如下：

| 优先级 | 近期任务 | 可量化产出 |
|---|---|---|
| P0 | 建立文献—数据—代码—产品版本台账 | 可追溯数据目录与处理规范 |
| P0 | 构建近岸湿对流层与条带误差诊断模块[7,11] | 残差场、协方差和误差预算 |
| P1 | 开展内潮/涡旋联合分离实验[1,6,19] | 相对经验方法的误差下降率 |
| P1 | 构建复杂河网动态中心线与拓扑[10,17–18] | 河道级 WSE、坡降和流量产品 |
| P1 | 建立 SWOT—多星测高多尺度融合[2,4,15] | 尺度依赖 RMSE 与谱保持率 |
| P2 | 开展潮间带和海底地形跨区泛化[12–14] | 独立区域 RMSE 与稳定性报告 |
| P2 | 发展 KaRIn SLC 拓展应用[3] | 标准处理链与示范数据集 |

## 8. 综合结论

SWOT 已经证明其不是传统测高任务的简单升级，而是一种新的二维水体高程观测范式。它在亚中尺度海洋动力、全球河流几何与蓄水、复杂河网、潮间带、海洋重力和海底地形方面打开了过去难以进入的研究空间[10,12–14,18–19]。

下一阶段的竞争焦点将从“是否能观测”转为“能否可靠解释”。最关键的科学与工程问题，是在小尺度上同时处理真实地球物理信号与结构化误差，并通过多源融合补足时间采样[1,4,7,11]。只有把误差模型、物理机制、机器学习和独立验证放进同一条处理链，SWOT 的高分辨率优势才会转化为稳定、可比较、可复现的科学知识和业务产品。

## 附录 A：文献分类与核心贡献

| 编号 | 文献主题 | 核心贡献 | 文献 |
|---|---|---|---|
| P01 | 全球内潮建模 | 数据同化模型预测非相干内潮，总内潮校正较经验方法降误差 59% | [1] |
| P02 | 南海细尺度涡识别 | 用 SWOT 验证 AVISO 与 2DVAR 涡旋边界，2DVAR 小尺度表现更好 | [2] |
| P03 | KaRIn 拓展应用 | 展示 SLC 单程 DInSAR、后向散射与相干性应用潜力 | [3] |
| P04 | SWOT—DUACS L3 融合 | 将二维刈幅数据纳入多星测高定标、清洗和融合体系 | [4] |
| P05 | 希腊湖泊水位 | PIXC 质量控制后湖泊平均水位达到约 13—19 cm 精度 | [5] |
| P06 | 全球内波数据集 | 构建 13 区、3,264 个内波信号的数据集，平均精度 91.21% | [6] |
| P07 | Bass Strait 几何验证 | 给出 2 km 产品 7 mm 噪声上限和主要误差来源 | [7] |
| P08 | 超强潮河口验证 | 校正后 L3 水位综合 RMSD 0.137 m | [8] |
| P09 | Death Valley 临时湖 | SWOT 水位与 OPERA 水域范围联合监测极端事件 | [9] |
| P10 | 辫状河多通道动力 | 动态中心线揭示支汊间 0.5 m 水位差和 2 cm/km 坡降差 | [10] |
| P11 | 湿对流层小尺度变化 | 15—80 km 残差可达误差预算两倍，近岸存在厘米级污染偏差 | [11] |
| P12 | 潮间带地形 | SWOT + Sentinel-2 生成 10 m DEM，多周期 RMSE 0.24 m | [12] |
| P13 | 高频海洋重力 | SWOT 在 2—4 km 点距上较 CryoSat-2 提升约 6.8%—7.9% | [13] |
| P14 | 深度学习海底地形 | SWOT 重力 + 船测水深 DNN 模型 RMS 97.5 m | [14] |
| P15 | 热带西太平洋亚中尺度涡 | SWOT 每子周期识别 273 个，DUACS 仅 13 个 | [15] |
| P16 | 全球内陆水位验证 | 系统评价湖泊和河流水位产品精度 | [16] |
| P17 | 全球河流流量框架 | 给出流量算法和完整不确定度预算 | [17] |
| P18 | 全球河道蓄水 | 126,674 个河段，估计全球年内蓄水变化范围 | [18] |
| P19 | 全球亚中尺度海洋动力 | 首次从全球视角展示亚中尺度涡和内孤立波 | [19] |

## 参考文献

> 以下题名链接均采用相对于本报告的路径。请将本报告保留在 SWOT 文件夹根目录，并与 `11_学术论文` 文件夹一同压缩、转发和解压。

[1] Yadidya B, Arbic B K, Zaron E D, et al. [A global internal tide modeling framework for improving satellite observations of fine-scale ocean circulation](./11_学术论文/01_海洋细尺度动力与多源融合/A%20global%20internal%20tide%20modeling%20framework%20for%20improving%20satellite%20observations%20of%20fine-scale%20ocean%20circulation.pdf)[J]. *Science Advances*, 2026, 12: eaee1885. DOI: 10.1126/sciadv.aee1885.

[2] Zhang X, et al. [Advances in Surface Water and Ocean Topography for fine-scale eddy identification from altimeter sea surface height merging maps in the South China Sea](./11_学术论文/01_海洋细尺度动力与多源融合/Advances%20in%20surface%20water%20and%20ocean%20topography%20for%20fine-scale%20eddy%20identification%20from%20altimeter%20sea%20surface%20height%20merging%20maps%20in%20the%20South%20China%20Sea.pdf)[J]. *Ocean Science*, 2025, 21: 1033–1045. DOI: 10.5194/os-21-1033-2025.

[3] GAMMA Remote Sensing AG. [Alternative applications of SWOT KaRIn time series](./11_学术论文/06_KaRIn拓展应用/Alternative%20applications%20of%20SWOT%20KaRIn%20time%20series.pdf)[C/OL]. 会议材料，出版时间未注明.

[4] Dibarboure G, Anadon C, Briol F, et al. [Blending 2D topography images from the Surface Water and Ocean Topography mission into the altimeter constellation with the Level-3 multi-mission Data Unification and Altimeter Combination System (DUACS)](./11_学术论文/01_海洋细尺度动力与多源融合/Blending%202D%20topography%20images%20from%20the%20Surface%20Water%20and%20Ocean%20Topography%20%28SWOT%29%20mission%20into%20the%20altimeter%20constellation%20with%20the%20Level-3%20multi-mission%20Data%20Unification%20and%20Altimeter%20Combination%20System%20%28DUACS%29.pdf)[J]. *Ocean Science*, 2025, 21: 283–323. DOI: 10.5194/os-21-283-2025.

[5] Ippeki T D, Grigoriadis V N. [Computation and validation of lake water levels in Greece using SWOT satellite data](./11_学术论文/02_内陆水文与河流湖泊/Computation%20and%20validation%20of%20lake%20water%20levels%20in%20Greece%20using%20SWOT%20satellite%20data.pdf)[J]. *Science China Earth Sciences*, 2026, 69(6): 2090–2101. DOI: 10.1007/s11430-025-1812-7.

[6] Xi X, Chen J, Chen G, et al. [Constructing a SWOT Internal Wave Dataset Using Deep Learning](./11_学术论文/01_海洋细尺度动力与多源融合/Constructing%20a%20SWOT%20Internal%20Wave%20Dataset%20Using%20Deep%20Learning_审稿期.pdf)[J]. *Earth System Science Data Discussions*, 2026. DOI: 10.5194/essd-2025-822.

[7] Hay A, Watson C, Legresy B, et al. [In situ geometric validation of SWOT satellite observations in Bass Strait, Australia](./11_学术论文/05_误差校正与定标验证/Earth%20and%20Space%20Science%20-%202025%20-%20Hay%20-%20In%20Situ%20Geometric%20Validation%20of%20SWOT%20Satellite%20Observations%20in%20Bass%20Strait%20.pdf)[J]. *Earth and Space Science*, 2025, 12: e2025EA004326. DOI: 10.1029/2025EA004326.

[8] Lichtman I D, Bell P S, Gommenginger C, et al. [Evaluating water levels from the Surface Water and Ocean Topography mission in a hyper-tidal coastal and estuarine environment](./11_学术论文/03_海岸带与潮间带/Earth%20and%20Space%20Science%20-%202025%20-%20Lichtman%20-%20Evaluating%20Water%20Levels%20From%20the%20Surface%20Water%20and%20Ocean%20Topography%20%20SWOT%20.pdf)[J]. *Earth and Space Science*, 2025, 12: e2024EA004104. DOI: 10.1029/2024EA004104.

[9] Buzzanga B, Hamlington B D, Bekaert D P S, et al. [Monitoring water from space: An illustration in Death Valley, California](./11_学术论文/02_内陆水文与河流湖泊/Geophysical%20Research%20Letters%20-%202025%20-%20Buzzanga%20-%20Monitoring%20Water%20From%20Space%20%20An%20Illustration%20in%20Death%20Valley%20%20California.pdf)[J]. *Geophysical Research Letters*, 2025, 52: e2024GL110250. DOI: 10.1029/2024GL110250.

[10] Franze S E, Köhn S, Chewning C, et al. [Braided rivers from SWOT: Water surface dynamics over the multi-channel Brahmaputra River](./11_学术论文/02_内陆水文与河流湖泊/Geophysical%20Research%20Letters%20-%202025%20-%20Franze%20-%20Braided%20Rivers%20From%20SWOT%20%20Water%20Surface%20Dynamics%20Over%20the%20Multi‐Channel.pdf)[J]. *Geophysical Research Letters*, 2025, 52: e2025GL116488. DOI: 10.1029/2025GL116488.

[11] Hay A, Watson C, Legresy B, et al. [Small scale variability in the wet troposphere impacts the interpretation of SWOT satellite observations](./11_学术论文/05_误差校正与定标验证/Geophysical%20Research%20Letters%20-%202025%20-%20Hay%20-%20Small%20Scale%20Variability%20in%20the%20Wet%20Troposphere%20Impacts%20the%20Interpretation%20of.pdf)[J]. *Geophysical Research Letters*, 2025, 52: e2024GL112778. DOI: 10.1029/2024GL112778.

[12] Sun M, Feng W, Wang X, et al. [Deriving intertidal topography from SWOT data and Sentinel-2 data](./11_学术论文/03_海岸带与潮间带/Geophysical%20Research%20Letters%20-%202025%20-%20Sun%20-%20Deriving%20Intertidal%20Topography%20From%20SWOT%20Data%20and%20Sentinel‐2%20Data.pdf)[J]. *Geophysical Research Letters*, 2025, 52: e2025GL117329. DOI: 10.1029/2025GL117329.

[13] Wang J, et al. [Improving high-frequency marine gravity anomaly recovery: The efficacy of SWOT wide-swath altimetry](./11_学术论文/04_海洋重力与海底地形/Improving_High-Frequency_Marine_Gravity_Anomaly_Recovery_The_Efficacy_of_SWOT_Wide-Swath_Altimetry.pdf)[J]. *IEEE Geoscience and Remote Sensing Letters*, 2024, 21: 1–5. DOI: 10.1109/LGRS.2024.3431694.

[14] Liu X, Hu M, Jin T. [Seafloor topography predicted from SWOT gravity data by deep neural network in the northwestern Pacific Ocean](./11_学术论文/04_海洋重力与海底地形/Seafloor%20topography%20predicted%20from%20SWOT%20gravity%20data%20by%20deep%20neural%20network%20in%20the%20northwestern%20Pacific%20Ocean.pdf)[J]. *Geophysical Journal International*, 2026, 244(3): ggag001. DOI: 10.1093/gji/ggag001.

[15] Cao L, Zhang Y, Wang Y, et al. [Submesoscale eddies identified by SWOT and their comparison with mesoscale eddies in the tropical western Pacific](./11_学术论文/01_海洋细尺度动力与多源融合/Submesoscale%20Eddies%20Identified%20by%20SWOT%20and%20Their%20Comparison%20with%20Mesoscale%20Eddies%20in%20the%20Tropical%20Western%20Pacific.pdf)[J]. *Remote Sensing*, 2025, 17(18): 3242. DOI: 10.3390/rs17183242.

[16] Yu L, Zhang H, Gong W, et al. [Validation of mainland water level elevation products from SWOT satellite](./11_学术论文/02_内陆水文与河流湖泊/Validation_of_Mainland_Water_Level_Elevation_Products_From_SWOT_Satellite.pdf)[J]. *IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing*, 2024, 17: 13494–13505. DOI: 10.1109/JSTARS.2024.3435363.

[17] Durand M, Gleason C J, Pavelsky T M, et al. [A framework for estimating global river discharge from the Surface Water and Ocean Topography satellite mission](./11_学术论文/02_内陆水文与河流湖泊/Water%20Resources%20Research%20-%202023%20-%20Durand%20-%20A%20Framework%20for%20Estimating%20Global%20River%20Discharge%20From%20the%20Surface%20Water%20and.pdf)[J]. *Water Resources Research*, 2023, 59: e2021WR031614. DOI: 10.1029/2021WR031614.

[18] Cerbelaud A, Wade J, David C H, et al. [Wide-swath altimetry maps bank shapes and storage changes in global rivers](./11_学术论文/02_内陆水文与河流湖泊/Wide-swath%20altimetry%20maps%20bank%20shapes%20and%20storage%20changes%20in%20global%20rivers.pdf)[J]. *Nature*, 2026, 651: 666–674. DOI: 10.1038/s41586-026-10218-y.

[19] Archer M, Wang J, Klein P, et al. [Wide-swath satellite altimetry unveils global submesoscale ocean dynamics](./11_学术论文/01_海洋细尺度动力与多源融合/Wide-swath%20satellite%20altimetry%20unveils%20global%20submesoscale%20ocean%20dynamics.pdf)[J]. *Nature*, 2025, 640: 691–696. DOI: 10.1038/s41586-025-08722-8.



