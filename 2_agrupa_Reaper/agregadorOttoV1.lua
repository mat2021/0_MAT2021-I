

function Msg(variable)
  reaper.ShowConsoleMsg(tostring(variable).."\n")
end


function read_lines(filepath)
  
  reaper.Undo_BeginBlock() -- Begin undo group
  
  local f = io.input(filepath)
  
  local snd = f:read ("*l") -- read one line
  repeat
    
    s = f:read ("*l") -- read one line
    
    if s then  -- if not end of file (EOF)
      t = {}
      for k, v in string.gmatch(s,"([^%s]+)") do
        t[k] = v
      end
      reaper.InsertMediaSection(snd, 1, t[2] / 32.0, t[3] / 32.0, 1)
    end
  
  until not s  -- until end of file

  f:close()

  reaper.Undo_EndBlock("Display script infos in the console", -1) -- End undo group
  
end

-- START -----------------------------------------------------
retval, filetxt = reaper.GetUserFileNameForRead("", "Import tracks from file", "txt")

if retval then 
  
  reaper.PreventUIRefresh(1)
  read_lines(filetxt)
  
  -- Update TCP
  reaper.TrackList_AdjustWindows(false)
  reaper.UpdateTimeline()
  
  reaper.UpdateArrange()
  reaper.PreventUIRefresh(-1)
  
end
