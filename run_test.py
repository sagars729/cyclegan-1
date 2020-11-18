import argparse
import os

parser = argparse.ArgumentParser(description='Generate Test Results While Training')
parser.add_argument("--models_dir", type=str, required=True, help="")
parser.add_argument("--log_dir", type=str, required=True, help="")
parser.add_argument("--config_filename", type=str, required=True, help="")
parser.add_argument("--skip", action="store_true", default=False)
parser.add_argument("--base_epoch", type=int, default=0)
parser.add_argument("--max_epoch", type=int, default=-1)
args = parser.parse_args()
epochs = set()
while True:
	files = os.listdir(args.models_dir)
	files = [int(i[9:-5]) for i in files if i[-5:] == ".meta"]
	files = sorted([i for i in files if i not in epochs])
	for e in files:
		if e < args.base_epoch: continue
		if args.max_epoch != -1 and e > args.max_epoch: continue
		epochs.add(e)
		print("Epoch", e)

		os.system("python main.py --to_train=0 --log_dir=%s --config_filename=%s --checkpoint_dir=%s --skip=%s --restore_epoch=%s" % (os.path.join(args.log_dir, str(e)), args.config_filename, args.models_dir, ("False", "True")[args.skip], e))

		date = [i for i in os.listdir(os.path.join(args.log_dir, str(e))) if os.path.isdir(os.path.join(args.log_dir, str(e), i)) and i != "fakes"][0]
		imgs = os.path.join(args.log_dir, str(e), date, "imgs")
		fakes = os.path.join(args.log_dir, str(e), "fakes")
		os.system("mkdir -p %s" % (os.path.join(fakes, "fakeA"),))
		os.system("mkdir -p %s" % (os.path.join(fakes, "fakeB"),))
		os.system("mkdir -p %s" % (os.path.join(fakes, "fakeAB"),))
		os.system("rsync -r --include='fakeA*' --exclude='*' %s %s" % (os.path.join(imgs, ""), os.path.join(fakes, "fakeA" , ""))) 
		os.system("rsync -r --include='fakeA*' --exclude='*' %s %s" % (os.path.join(imgs, ""), os.path.join(fakes, "fakeAB", ""))) 
		os.system("rsync -r --include='fakeB*' --exclude='*' %s %s" % (os.path.join(imgs, ""), os.path.join(fakes, "fakeB" , "")))
		os.system("rsync -r --include='fakeB*' --exclude='*' %s %s" % (os.path.join(imgs, ""), os.path.join(fakes, "fakeAB", "")))
		

