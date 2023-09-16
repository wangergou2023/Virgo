export RK_ARCH :=arm64
export RK_CROSS := aarch64-linux-gnu-
export RK_CONFIG := lubancat2_defconfig
export RK_KERNEL_DTS :=rk3568-lubancat-2-v1
export RK_SOURCE_DIR=$(shell pwd)/../src


all:
# 加载配置文件
	${MAKE} -C ../src ARCH=$(RK_ARCH) CROSS_COMPILE=$(RK_CROSS) $(RK_CONFIG)
# 构建Debian二进制包
	${MAKE} -C ../src ARCH=$(RK_ARCH) CROSS_COMPILE=$(RK_CROSS) RK_KERNEL_DTS=$(RK_KERNEL_DTS) bindeb-pkg
# 构建img镜像
	${MAKE} -C ../src ARCH=$(RK_ARCH) CROSS_COMPILE=$(RK_CROSS) $(RK_KERNEL_DTS).img
# 使用dtbs参数单独编译设备树
	${MAKE} -C ../src ARCH=$(RK_ARCH) CROSS_COMPILE=$(RK_CROSS) dtbs
# 打包成extboot分区
	chmod 777 $(RK_SOURCE_DIR)/extboot.sh
	cd $(RK_SOURCE_DIR);./extboot.sh 

clean:
	@$(MAKE) -C $(RK_SOURCE_DIR)/ distclean
	-@rm ../bin/* -rf
	-@rm ../src/arch/arm/boot/Image* -rf
	-@rm ../src/arch/arm/boot/uImage* -rf
	-@rm ../linux-*.buildinfo ../linux-*.changes -rf 
	-@rm ../linux-headers-*.deb ../linux-image-*.deb ../linux-libc-dev*.deb -rf
