import os
import json
import datetime
import shutil

history_dirs = [
    os.path.join(os.environ['APPDATA'], 'Code', 'User', 'History'),
    os.path.join(os.environ['APPDATA'], 'Cursor', 'User', 'History'),
    os.path.join(os.environ['APPDATA'], 'Windsurf', 'User', 'History')
]

current_time = datetime.datetime.now()
target_time = current_time - datetime.timedelta(hours=24) # Look at last 24 hours

results = []

for history_dir in history_dirs:
    if not os.path.exists(history_dir): continue
    for folder in os.listdir(history_dir):
        folder_path = os.path.join(history_dir, folder)
        if not os.path.isdir(folder_path): continue
        
        entries_file = os.path.join(folder_path, 'entries.json')
        if not os.path.exists(entries_file): continue
    
        try:
            with open(entries_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            res = data.get('resource', '')
                
            entries = data.get('entries', [])
            if not entries: continue
            
            # Find entries modified in the last 24 hours
            recent_entries = []
            for entry in entries:
                if 'timestamp' in entry:
                    ts = entry['timestamp'] / 1000.0
                    dt = datetime.datetime.fromtimestamp(ts)
                    if dt > target_time:
                        entry_path = os.path.join(folder_path, entry['id'])
                        if os.path.exists(entry_path):
                            recent_entries.append((dt, entry_path))
            
            if recent_entries:
                recent_entries.sort(key=lambda x: x[0], reverse=True)
                latest_backup = recent_entries[0]
                results.append((res, latest_backup[0], latest_backup[1]))
                
        except Exception as e:
            pass

results.sort(key=lambda x: x[1], reverse=True)
print(f"Total AB_AI files with recent backups: {len(results)}")
for res, dt, backup_path in results:
    print(f"{dt} -- {res}")
    # Optional: print out where the backup is so we can manually copy it
    # print(f"  Backup File: {backup_path}")
    
# Let's save the mapping so we can restore them
with open('recent_backups.json', 'w') as f:
    json.dump([{'target': r[0], 'time': r[1].isoformat(), 'backup': r[2]} for r in results], f, indent=2)
