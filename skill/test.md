###从单元测试为什么半途而废说起
- 场景1：紧急修复bug，手动测了没问题直接上了，测试代码的"回头改"变成了"没有改"；或者是开发过程中接口变动，
任务紧，就没有改对应的测试代码
  - **注意点1：改bug或改接口前先改测试代码，保持测试代码100%的通过率；自己的代码自己写测试**
- 场景2：测试代码和主代码都改了，但一跑测试代码发现祖国江山一片红，遂放弃
  - 原因分析
    - 场景1中的情况没有避免
    - 改代码所引起的问题，这也正是单元测试在发挥作用，唯有老实修复为上
    - 测试代码冗余，同一个逻辑多次检查，所以当此逻辑变化时，就会带来改测试代码代价太高的问题。比如创建
    文章这一逻辑，在发布文章和发布首页里都会用到，但是只应该在文章增删查改这一单元里验证一次，甚至只调
    用这一次，其它地方当需要这一数据时用sql插入或者用其它方法初始化数据，又或者文章发布的测试跟在文章
    增删查改测试的后面形成一条测试链路
  - **注意点2：不重复检查逻辑；测试代码逻辑尽可能简单，本身不要有bug**
- 场景3：完整的跑一遍测试花的时间过长，于是只跑相关单元测试
  - **注意点3：提高测试代码的运行效率；引入持续集成**
###其它
- 关于持续集成的理解：当代码提交到线上时，会在正式环境的副本上完整的跑一次测试，通过后再正式发布
- 关于是否需要回收数据的想法：由于测试代码中大约80%都涉及到发布流程，所以只有剩余的少部分测试代码能在正
式环境上跑；又因为上一条对持续集成的理解，我们不需要在正式环境中跑测试代码，所以我们不需要做严格的数据
回收，这样也方便形成测试链路，以及减少测试代码运行的时间
