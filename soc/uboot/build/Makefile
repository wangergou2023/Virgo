CROSS := aarch64-linux-gnu-
CONFIG := rk3568_defconfig

SOURCE_DIR=$(shell pwd)/../src
RKBIN = $(PWD)/../rkbin

all:
	$(MAKE) -C ../src CROSS_COMPILE=$(CROSS) $(CONFIG) 
	$(MAKE) -C ../src CROSS_COMPILE=$(CROSS)
	cd $(SOURCE_DIR);./scripts/fit.sh  --ini-trust $(RKBIN)/RKTRUST/RK3568TRUST.ini --ini-loader $(RKBIN)/RKBOOT/RK3568MINIALL.ini --chip RK3568
clean:
	@$(MAKE) -C $(SOURCE_DIR)/ distclean
	-@rm ../bin/* -rf
