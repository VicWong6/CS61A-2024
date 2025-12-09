1. lab0 的课程网址：https://insideempire.github.io/CS61A-Website-Archive/lab/lab00.html

   评分后续会同步到这个地址：https://okpy.org/cal/cs61a/fa24/lab00/

   前辈的学习记录：https://ajohn.top/cs61a/lab-lab00/

   okpy的玩法：https://ok-help.cs61a.org/

   # 疑问

   1. 登录不了gradescope ，不知道**Course Entry Code。**
   2. 现在可以登录OK，但是提交不了东西。
   3. OK可以本地运行，得到结果。

   ```bash
   python3 ok --local
   ```

   # 原文抄录：

   ## Appendix: Useful Python Command Line Options

   附录：有用的Python命令行选项

   Here are the most common ways to run Python on a file.

   1. Using no command-line options will run the code in the file you provide and return you to the command line. If your file just contains function definitions, you'll see no output unless there is a syntax error.不使用命令行选项将运行你提供的文件中的代码，并返回到命令行。如果你的文件只包含函数定义，除非存在语法错误，否则你将看不到任何输出。

      ```
      python3 lab00.py
      ```

   2. **`i`**: The `i` option runs the code in the file you provide, then opens an interactive session (with a `>>>` prompt). You can then evaluate expressions, for example calling functions you defined. To exit, type `exit()`. You can also use the keyboard shortcut `Ctrl-D` on Linux/Mac machines or `Ctrl-Z Enter` on Windows.

      **`i`**：`i`选项会运行你提供的文件中的代码，然后打开一个交互式会话（带有`>>>`提示符）。之后你可以计算表达式，例如调用你定义的函数。要退出，请输入`exit()`。你也可以在Linux/Mac电脑上使用键盘快捷键`Ctrl-D`，或在Windows上使用`Ctrl-Z Enter`。

      If you edit the Python file while running it interactively, you will need to exit and restart the interpreter in order for those changes to take effect.

      Here's how we can run `lab00.py` interactively:

      ```
      python3 -i lab00.py
      ```

   3. **`m doctest`**: Runs the doctests in a file, which are the examples in the docstrings of functions.

      Each test in the file consists of `>>>` followed by some Python code and the expected output.

      Here's how we can run the doctests in `lab00.py`:

      ```
       python3 -m doctest lab00.py
      ```

      When our code passes all of the doctests, no output is displayed. Otherwise, information about the tests that failed will be displayed.



测试地址：https://www.bilibili.com/video/BV1sy411z7nA/?spm_id_from=333.337.search-card.all.click&vd_source=5fddd813efee356467a7e0a5aed5c1d9