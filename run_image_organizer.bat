@echo off
:: 图片整理脚本启动器 - 需要管理员权限
:: 此脚本会自动请求管理员权限并运行图片整理程序

title 图片整理脚本 - 管理员权限

:: 检查是否以管理员权限运行
net session >nul 2>&1
if %errorLevel% == 0 (
    echo.
    echo ================================================
    echo         图片整理脚本 - 管理员权限已确认
    echo ================================================
    echo.
    echo 正在启动图片整理程序...
    echo.
    python image_organizer.py
    echo.
    echo 脚本执行完成！按任意键退出...
    pause >nul
) else (
    echo.
    echo ================================================
    echo         需要管理员权限
    echo ================================================
    echo.
    echo 图片整理脚本需要管理员权限来访问所有文件。
    echo 正在请求管理员权限...
    echo.
    :: 使用PowerShell提升权限并重新运行此脚本
    powershell "start-process '%~f0' -verb runas"
    exit /b
)