# Save to:
# ~/Library/Application Support/Sublime Text 3/Packages/ToggleSideBarWithFocus.py
import sublime
import sublime_plugin

class ToggleSideBarWithFocusCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.window.run_command("toggle_side_bar")
    if self.window.is_sidebar_visible():
      self.window.run_command("focus_side_bar")
    else:
      self.window.run_command("focus_group", { 'group': 0 })
