const { spawn, execFile } = require("child_process");
console.log("./dist/scanBle/scanBle.exe");
const ls = execFile("./dist/scanBle/scanBle.exe", (error, stdout, stderr) => {
  if (error) {
    throw error;
  }
  console.log(stdout);
});
