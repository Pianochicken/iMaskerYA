<template>
  <q-page class="flex flex-center">
    <img
      style="position:absolute; background-position:center center; z-index: -100;"
      alt="iMaskerYA"
      src="../images/ntpu_background.gif"
    >
    <q-card flat class="row col-12 justify-center" style="width:90%; height:500px">
        <q-tabs
          v-model="date_choose"
          vertical
          indicator-color="transparent"
          active-color="black"
          content-class="tab-text"
          class="text-grey-4 shadow-2 text-bold "
          style="font-family:Microsoft JhengHei; font-weight:bold; font-size:30px;"
        >
          <q-tab name="three" icon="img:three.png" label="三天" />
          <q-tab name="seven" icon="img:seven.png" label="一週" />
          <q-tab name="thirty" icon="img:month.png" label="一個月" />
        </q-tabs>
      
      <!-- <q-btn-toggle class="col-2"
        v-model="date_choose"
        bounded
        color="grey"
        text-color="white"
        toggle-color="primary"
        toggle-text-color="white"
        :options="[
          {label: '一般', value: 'normal', style:'font-size:16px; font-weight:bold; font-family:Microsoft JhengHei;'},
          {label: '溫柔', value: 'kind', style:'font-size:16px; font-weight:bold; font-family:Microsoft JhengHei;'},
          {label: '大罵', value: 'shouting', style:'font-size:16px; font-weight:bold; font-family:Microsoft JhengHei;'}
        ]"
      /> -->
      <!-- <div class="q-pa-md line-wrap col-12" id="chartLine"></div> -->
      <div class="q-pa-md col" ref="chartLine"></div>
    </q-card>

    
  </q-page>
</template>

<script>
var datearr = [];
var allcountarr = [];
var nomaskcountarr = [];

import fs from "fs";
import path from "path";

import * as echarts from "echarts";
// require("echarts/theme/dark"); //引入主题

export default {
  data() {
    return {
      date_choose: 'three',
      chartLine: null,
      chart_date_text: '3',
      search_number: 3,
    };
  },
  mounted() {
    var Today = new Date();

    datearr = []
    allcountarr = []
    nomaskcountarr = []
    
    for (var daycount = 0; daycount < this.search_number; daycount++) {
      // console.log("今天日期是 " + Today.getFullYear() + " 年 " + (Today.getMonth() + 1) + " 月 " + Today + " 日");
      //讀取txt並轉換為json
      try {
        let fileContents = fs.readFileSync(
          path.join(
            __statics,'../darknet/build/darknet/x64/' +
            Today.getFullYear() +
              "_" +
              (Today.getMonth() + 1) +
              "_" +
              Today.getDate() +
              ".txt"
          ), "utf8"
        );

      fileContents = fileContents.slice(0, fileContents.length - 3);
      fileContents = "[" + fileContents + "]";

      // console.log("fileContents: ", fileContents)
      // console.log("open file name: ", Today.getFullYear() +"_" + (Today.getMonth() + 1) + "_" + Today.getDate() + ".txt")
      var json_data = JSON.parse(fileContents);

      let allcount = 0;
      let nomaskcount = 0;

      for (var i = 0; i < json_data.length; i++) {
        for (var j = 0; j < json_data[i].objects.length; j++) {
          //計算總人數
          allcount++;
          if (json_data[i].objects[j].name == "no mask") {
            //未戴口罩人數
            nomaskcount++;
          }
        }
      }
      datearr.push(Today.getMonth() + 1 + "/" + Today.getDate());
      allcountarr.push(Math.round(allcount/3));
      nomaskcountarr.push(Math.round(nomaskcount/6));
      Today.setDate(Today.getDate() - 1);
      } catch (err) {
        break;
        console.log("error: ", err)
        // Here you get the error when the file was not found,
        // but you also get any other error
      }
    }
    datearr = datearr.reverse()
    allcountarr = allcountarr.reverse()
    nomaskcountarr = nomaskcountarr.reverse()
    // console.log("datearr: ", datearr)
    // console.log("allcountarr: ", allcountarr)
    // console.log("nomaskcountarr: ", nomaskcountarr)

    this.$nextTick(() => {
      this.drawLineChart();
    });
  },
  methods: {
    drawLineChart() {
      let bar_dv = this.$refs.chartLine;
      this.chartLine = echarts.init(bar_dv); // 初始化echarts
      // this.chartLine = echarts.init(this.$el, "day"); // 初始化echarts
      let option = {
        title: {
          text: this.chart_date_text + " 日內人流統計",
          subtext: "",
        },
        tooltip: {
          trigger: "axis",
        },
        legend: {
          data: ["總人數", "未戴口罩"],
        },
        toolbox: {
          show: true,
          feature: {
            mark: { show: true },
            dataView: { show: true, readOnly: false },
            magicType: { show: true, type: ["line", "bar", "stack", "tiled"] },
            restore: { show: true },
            saveAsImage: { show: true },
          },
        },
        calculable: true,
        xAxis: [
          {
            type: "category",
            boundaryGap: false,
            data: datearr,
          },
        ],
        yAxis: [
          {
            type: "value",
          },
        ],
        series: [
          {
            name: "總人數",
            type: "line",
            itemStyle: { normal: { areaStyle: { type: "default" } } },
            data: allcountarr,
          },
          {
            name: "未戴口罩",
            type: "line",
            itemStyle: { normal: { areaStyle: { type: "default" } } },
            data: nomaskcountarr,
          },
        ],
      };
      // 使用剛指定的配置項目和數據顯示圖表
      this.chartLine.setOption(option);
    },
  },
  watch: {
    date_choose(){
      console.log("this.date_choose: ", this.date_choose)
      if(this.date_choose === 'three'){
        this.chart_date_text = '3'
        this.search_number = 3
      }
      else if (this.date_choose === 'seven'){
        this.chart_date_text = '7'
        this.search_number = 7
      }
      else if (this.date_choose === 'thirty'){
        this.chart_date_text = '30'
        this.search_number = 30
      }
      datearr = []
      allcountarr = []
      nomaskcountarr = []

      var Today = new Date();
      for (var daycount = 0; daycount < this.search_number; daycount++) {
        // console.log("今天日期是 " + Today.getFullYear() + " 年 " + (Today.getMonth() + 1) + " 月 " + Today + " 日");
        //讀取txt並轉換為json

        console.log("daycount: ", daycount, "  this.search_number: ", this.search_number)
        try {
          let fileContents = fs.readFileSync(
            path.join(
              __statics,'../darknet/build/darknet/x64/' +
              Today.getFullYear() +
                "_" +
                (Today.getMonth() + 1) +
                "_" +
                Today.getDate() +
                ".txt"
            ), "utf8"
          );

        fileContents = fileContents.slice(0, fileContents.length - 3);
        fileContents = "[" + fileContents + "]";

        // console.log("fileContents: ", fileContents)
        // console.log("open file name: ", Today.getFullYear() +"_" + (Today.getMonth() + 1) + "_" + Today.getDate() + ".txt")
        var json_data = JSON.parse(fileContents);

        let allcount = 0;
        let nomaskcount = 0;

        for (var i = 0; i < json_data.length; i++) {
          for (var j = 0; j < json_data[i].objects.length; j++) {
            //計算總人數
            allcount++;
            if (json_data[i].objects[j].name == "no mask") {
              //未戴口罩人數
              nomaskcount++;
            }
          }
        }
        datearr.push(Today.getMonth() + 1 + "/" + Today.getDate());
        allcountarr.push(Math.round(allcount/3));
        nomaskcountarr.push(Math.round(nomaskcount/6));
        Today.setDate(Today.getDate() - 1);
        } catch (err) {
          break;
          console.log("error: ", err)
          // Here you get the error when the file was not found,
          // but you also get any other error
        }
      }
      datearr = datearr.reverse()
      allcountarr = allcountarr.reverse()
      nomaskcountarr = nomaskcountarr.reverse()



      this.$nextTick(() => {
        this.drawLineChart();
        window.addEventListener("resize", this.chartLine.resize);
      });
    }
  }
};
</script>

<style lang="sass" scope>
.line-wrap 
  width: 500%
  height: 500px

.tab-text
  font-family: "Microsoft JhengHei"
  font-weight: "bold"
</style>

